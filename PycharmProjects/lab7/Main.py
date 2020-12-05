from DataReader import DataParser
from Perceptron import Perceptron


def divide_train_test_data(data, labels, divisor):
    if data.shape[0] != labels.shape[0]:
        raise ValueError('Data rows number has to be the same as labels number')
    if divisor >= data.shape[0] or divisor <= 0:
        raise ValueError(f'Divisor has to be a number from 1 to {data.shape[0]}')
    train_data = data[:divisor]
    test_data = data[divisor:]
    train_labels = labels[:divisor]
    test_labels = labels[divisor:]
    return train_data, test_data, train_labels, test_labels


if __name__ == '__main__':
    dp = DataParser()
    dp.read_data_as_arr("sample3.csv") # alternatywnie mozna podmienic na sample1, sample2 i sample3
    dp.normalize_rows()
    p = Perceptron()
    train_data, test_data, train_labels, test_labels = divide_train_test_data(dp.data_arr, dp.label, 30)
    p.train(train_data, train_labels)
    predicted = p.predict(test_data)
    print(f'actual: {test_labels}')
    print(f'predicted: {predicted}')
    print(p.check_precision(test_labels, predicted))


