# Write your code here
filename: str = 'flowers.txt'

# HINT: create a dictionary from flowers.txt
flower_dict = {}
with open(filename, 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        parts = [x.strip() for x in str.split(line, ':')]
        flower_dict[parts[0].upper()] = parts[1]

# HINT: create a function to ask for user's first and last name
def get_name():
    full_name = input("Enter your First [space] Last name only: ")
    return full_name

# print the desired output
name: str = get_name()
print(f'Unique flower name with the first letter: {flower_dict[name[0].upper()]}')

