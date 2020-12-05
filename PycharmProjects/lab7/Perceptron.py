import numpy as np


# jako dodatkowa pomoc służył mi filmik https://www.youtube.com/watch?v=t2ym2a3pb_Y
class Perceptron:

    def __init__(self, learning_rate=0.01, number_of_iterations=1000):
        self.learning_rate = learning_rate
        self.number_of_iterations = number_of_iterations
        self.activation_func = self.unit_step
        self.weights = None
        self.bias = None

    def train(self, train_data, train_label):
        rows, columns = np.array(train_data).shape  # n - rows: samples, m - columns: features
        self.weights = np.zeros(columns)  # inicjalizacja wag, na początku zera
        self.bias = 0
        for x in range(self.number_of_iterations):  # wykonujemy np. 1000 iteracji, aby nauczyć model
            for i, current_data in enumerate(train_data):  # iterujemy się po danych wejściowych
                linear_out = np.dot(current_data, self.weights) + self.bias  # mnożenie danych przez wagi i dodanie ewentualnego biasu
                predicted = self.activation_func(linear_out)  # liczymy wartość przewidywaną
                update = self.learning_rate * (train_label[i] - predicted)  # aktualizacja wag na podstawie różnicy faktycznej wartości z zaprognozowaną
                self.weights += update * current_data
                self.bias += update

    def predict(self, data_arr):
        linear_out = np.dot(data_arr, self.weights) + self.bias
        predicted = self.activation_func(linear_out)
        return predicted

    def unit_step(self, val):
        return np.where(val >= 0, 1, 0)  # zadziala zarowno dla 1 wartosci, jak i dla wielu w wektorze

    def check_precision(self, actual, predicted):
        precision = np.sum(actual == predicted) / len(actual)
        return precision
