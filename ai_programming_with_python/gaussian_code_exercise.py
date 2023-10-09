from gaussian import Gaussian

gaussian = Gaussian(25, 2)
gaussian.read_data_file('files/numbers.txt')
gaussian.plot_histogram()