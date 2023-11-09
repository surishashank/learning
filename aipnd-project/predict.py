import sys
import argparse
import logging
import utils


def main():
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description='Predict Type of Flower')
    parser.add_argument('image_path', type=str, metavar='', help='Path to image file to predict')
    parser.add_argument('-k', '--top_k', dest='top_k', type=int, required=False, metavar='',
                        help='Top K most likely classes. Default = 1')
    parser.add_argument('-c', '--category_names', dest='category_names', type=str, required=False, metavar='',
                        help='JSON file mapping categories to real names. Default = None')
    parser.add_argument('-g', '--gpu', dest='gpu', action='store_true', help='Use GPU for inference')

    args: argparse.Namespace = parser.parse_args()

    logging.info(f'Running command: python {" ".join(sys.argv)}')
    top_k: int = args.top_k if args.top_k else 1

    predict(args.image_path, top_k, args.category_names, args.gpu)


def predict(image_path: str, top_k: int, category_names: str, gpu: bool) -> None:
    return

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(name)s %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logging.Formatter(datefmt='%Y-%m-%d %H:%M:%S')
    main()

