import sys
import argparse
import logging
import utils


def main():
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description='Train a new network on a data set')
    parser.add_argument('data_dir', type=str, metavar='', help='Path to data directory')
    parser.add_argument('-s', '--save_dir', dest='save_dir', type=str, required=False, metavar='',
                        help='Directory to save checkpoints. Default = current directory')
    parser.add_argument('-a', '--arch', dest='arch', type=str, required=False, metavar='',
                        help='Model architecture. Default = vgg16')
    parser.add_argument('-l', '--learning_rate', dest='learning_rate', type=float, required=False, metavar='',
                        help='Learning rate. Default = 0.001')
    parser.add_argument('-u', '--hidden_units', dest='hidden_units', type=int, required=False, metavar='',
                        help='Number of hidden units. Default = 4096')
    parser.add_argument('-e', '--epochs', dest='epochs', type=int, required=False, metavar='',
                        help='Number of epochs. Default = 3')

    args: argparse.Namespace = parser.parse_args()

    logging.info(f'Running command: python {" ".join(sys.argv)}')
    save_dir: str = args.save_dir if args.save_dir else '.'
    arch: str = args.arch if args.arch else 'vgg16'
    learning_rate: float = args.learning_rate if args.learning_rate else 0.001
    hidden_units: int = args.hidden_units if args.hidden_units else 4096
    epochs: int = args.epochs if args.epochs else 3

    train(args.data_dir, save_dir, arch, learning_rate, hidden_units, epochs)


def train(data_dir: str, save_dir: str, arch: str, learning_rate: float, hidden_units: int, epochs: int) -> None:
    return


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(name)s %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logging.Formatter(datefmt='%Y-%m-%d %H:%M:%S')
    main()





