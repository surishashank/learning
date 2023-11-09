import numpy as np
import torch
from torch import nn
from torchvision import datasets, transforms, models
import json
from typing import Dict, List, Tuple, Union, Optional, Any
from PIL import Image

data_dir = 'flowers'
train_key = 'train'
valid_key = 'valid'
test_key = 'test'

train_dir = data_dir + '/' + train_key
valid_dir = data_dir + '/' + valid_key
test_dir = data_dir + '/' + test_key

# Define transforms for the training, validation, and testing sets
data_transforms = {
    train_key: transforms.Compose([transforms.RandomRotation(30),  # Rotate image by 30 degrees
                                   transforms.RandomResizedCrop(224),  # Crop image to 224x224 pixels
                                   transforms.RandomHorizontalFlip(),  # Flip image horizontally
                                   transforms.ToTensor(),  # Convert image to PyTorch tensor
                                   transforms.Normalize([0.485, 0.456, 0.406],  # Normalize image for pre-trained model
                                                        [0.229, 0.224, 0.225])]),
    valid_key: transforms.Compose([transforms.Resize(224),  # Resize image to 224 pixels
                                   transforms.CenterCrop(224),  # Crop image to 224x224 pixels
                                   transforms.ToTensor(),  # Convert image to PyTorch tensor
                                   transforms.Normalize([0.485, 0.456, 0.406],  # Normalize image for pre-trained model
                                                        [0.229, 0.224, 0.225])]),
    test_key: transforms.Compose([transforms.Resize(224),  # Resize image to 224 pixels
                                  transforms.CenterCrop(224),  # Crop image to 224x224 pixels
                                  transforms.ToTensor(),  # Convert image to PyTorch tensor
                                  transforms.Normalize([0.485, 0.456, 0.406],  # Normalize image for pre-trained model
                                                       [0.229, 0.224, 0.225])])
}

# Load the datasets with ImageFolder
image_datasets = {
    train_key: datasets.ImageFolder(train_dir, transform=data_transforms[train_key]),
    valid_key: datasets.ImageFolder(valid_dir, transform=data_transforms[valid_key]),
    test_key: datasets.ImageFolder(test_dir, transform=data_transforms[test_key])
}

# Using the image datasets and the trainforms, define the dataloaders
dataloaders = {
    train_key: torch.utils.data.DataLoader(image_datasets[train_key], batch_size=64, shuffle=True),
    valid_key: torch.utils.data.DataLoader(image_datasets[valid_key], batch_size=64),
    test_key: torch.utils.data.DataLoader(image_datasets[test_key], batch_size=64)
}

with open('cat_to_name.json', 'r') as f:
    cat_to_name = json.load(f)

# load pre-trained model VGG19_BN
model = models.vgg19_bn(weights=models.VGG19_BN_Weights.IMAGENET1K_V1)
# print(model)
# Freeze parameters so we don't backprop through them
for param in model.parameters():
    param.requires_grad = False

# Define a new, untrained feed-forward network as a classifier, using ReLU activations and dropout
classifier = nn.Sequential(nn.Linear(25088, 4096),
                           nn.ReLU(),
                           nn.Dropout(0.2),
                           nn.Linear(4096, 102),
                           nn.LogSoftmax(dim=1))

# Replace the pre-trained classifier with our new classifier
model.classifier = classifier

# Use GPU if it's available
def get_device() -> torch.device:
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")
device = get_device()
model.to(device)

# Define loss and optimizer
criterion = nn.NLLLoss()
optimizer = torch.optim.Adam(model.classifier.parameters(), lr=0.001)

# Train the classifier layers using backpropagation using the pre-trained network to get the features
epochs = 3
steps = 0
running_loss = 0
print_every = 20

for epoch in range(1, epochs+1):
    for inputs, labels in dataloaders[train_key]:
        steps += 1
        # Move input and label tensors to the default device
        inputs, labels = inputs.to(device), labels.to(device)

        # Clear the gradients, do this because gradients are accumulated
        optimizer.zero_grad()

        # Forward pass, then backward pass, then update weights
        logps = model.forward(inputs)
        loss = criterion(logps, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

        # Track the loss and accuracy on the validation set to determine the best hyperparameters
        if steps % print_every == 0:
            valid_loss = 0
            accuracy = 0
            model.eval()

            with torch.no_grad():
                for inputs, labels in dataloaders[valid_key]:
                    inputs, labels = inputs.to(device), labels.to(device)
                    logps = model.forward(inputs)
                    batch_loss = criterion(logps, labels)

                    valid_loss += batch_loss.item()

                    # Calculate accuracy
                    ps = torch.exp(logps)
                    top_ps, top_class = ps.topk(1, dim=1)
                    equals = top_class == labels.view(*top_class.shape)
                    accuracy += torch.mean(equals.type(torch.FloatTensor)).item()

            print(f'Epoch: {epoch}/{epochs}')
            print(f'Training loss: {running_loss/print_every:.3f}')
            print(f'Validation loss: {valid_loss/len(dataloaders[valid_key]):.3f}')
            print(f'Validation accuracy: {accuracy/len(dataloaders[valid_key]):.3f}')

            running_loss = 0
            model.train()

# Test the trained network
test_loss = 0
accuracy = 0
model.eval()

with torch.no_grad():
    for inputs, labels in dataloaders[test_key]:
        inputs, labels = inputs.to(device), labels.to(device)
        logps = model.forward(inputs)
        batch_loss = criterion(logps, labels)

        test_loss += batch_loss.item()

        # Calculate accuracy
        ps = torch.exp(logps)
        top_ps, top_class = ps.topk(1, dim=1)
        equals = top_class == labels.view(*top_class.shape)
        accuracy += torch.mean(equals.type(torch.FloatTensor)).item()

    print(f'Test loss: {test_loss/len(dataloaders[test_key]):.3f}')
    print(f'Test accuracy: {accuracy/len(dataloaders[test_key]):.3f}')


# Save the checkpoint
model.class_to_idx = image_datasets[train_key].class_to_idx
checkpoint = {'input_size': 25088,
              'output_size': 102,
              'hidden_layers': [4096],
              'dropout': [0.2],
              'state_dict': model.state_dict(),
              'class_to_idx': model.class_to_idx,
              'optimizer_state_dict': optimizer.state_dict(),
              'epochs': epochs,
              'classifier': classifier,
              'criterion': criterion
              }
torch.save(checkpoint, 'checkpoint.pth')

# Load the checkpoint
def load_checkpoint(filepath):
    checkpoint = torch.load(filepath)
    model = models.vgg19_bn(weights=models.VGG19_BN_Weights.IMAGENET1K_V1)
    model.classifier = checkpoint['classifier']
    model.load_state_dict(checkpoint['state_dict'])
    model.class_to_idx = checkpoint['class_to_idx']
    return model

def process_image(image_path: str) -> np.array:
    ''' Scales, crops, and normalizes a PIL image for a PyTorch model,
        returns an Numpy array
    '''
    # Process a PIL image for use in a PyTorch model
    image: Image.Image = Image.open(image_path)

    # resize the images where the shortest side is 256 pixels, keeping the aspect ratio
    width, height = image.size
    if width < height:
        image.thumbnail((256, 1000000))
    else:
        image.thumbnail((1000000, 256))

    # crop out the center 224x224 portion of the image
    width, height = image.size
    left: int = int((width - 224) / 2)
    top: int = int((height - 224) / 2)
    right: int = int((width + 224) / 2)
    bottom: int = int((height + 224) / 2)
    image = image.crop((left, top, right, bottom))

    # convert color channels to 0-1
    np_image: np.array = np.array(image) / 255
    # normalize the image
    np_image = (np_image - np.array([0.485, 0.456, 0.406])) / np.array([0.229, 0.224, 0.225])
    # transpose the image
    np_image = np_image.transpose((2, 0, 1))

    return np_image

def predict(image_path: str, model: nn.Module, topk: int = 5) -> Tuple[List[float], List[str]]:
    # Predict the class (or classes) of an image using a trained deep learning model.
    image: np.array = process_image(image_path)
    image_tensor: torch.Tensor = torch.from_numpy(image).type(torch.FloatTensor)
    image_tensor.unsqueeze_(0)
    image_tensor = image_tensor.to(get_device())
    model.eval()
    with torch.no_grad():
        logps: torch.Tensor = model.forward(image_tensor)
        ps: torch.Tensor = torch.exp(logps)
        top_ps, top_class = ps.topk(topk, dim=1)
        top_ps: List[float] = top_ps.cpu().numpy()[0]
        top_class: List[int] = top_class.cpu().numpy()[0]
        idx_to_class: Dict[int, str] = {v: k for k, v in model.class_to_idx.items()}
        top_class: List[str] = [idx_to_class[i] for i in top_class]
    return top_ps, top_class

new_model = load_checkpoint('checkpoint.pth')
test_image_path = 'flowers/test/101/image_07988.jpg'
top_ps, top_classes = predict(test_image_path, new_model)
top_names = [cat_to_name[i] for i in top_classes]

# Display an image along with the top 5 classes
top_ps, top_classes = zip(*sorted(zip(top_ps, top_classes)))
fig, (ax1, ax2) = plt.subplots(figsize=(6, 9), ncols=1, nrows=2)
ax1.axis('off')
ax1.set_title(top_names[0])
ax1.imshow(Image.open(test_image_path))
ax2.barh(np.arange(5), top_ps)
ax2.set_aspect(0.1)
ax2.set_yticks(np.arange(5))
ax2.set_yticklabels(top_names)
ax2.set_title('Class Probability')
ax2.set_xlim(0, 1.1)
plt.tight_layout()
plt.show()
