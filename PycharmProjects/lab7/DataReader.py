import csv
import numpy as np


class DataParser:

    def __init__(self):
        self.data_arr = None
        self.label = None

    def read_data_as_arr(self, path, label=-1, delimiter=';'):
        arr = np.genfromtxt(path, delimiter=delimiter, dtype=float)
        if label is not None:
            self.label = arr[:, label]
            self.data_arr = np.delete(arr, label, axis=1)

    def normalize_column(self, col_number):  # przez standaryzację
        self.data_exists()
        column = self.data_arr[:, col_number]
        mean = column.mean()
        std = column.std()
        if std != 0:
            self.data_arr[:, col_number] = (column - mean) / std

    def normalize_rows(self):  # przez standaryzację
        self.data_exists()
        i = 0
        while i < self.data_arr.shape[0]:   # numpy wykonuje operacje element po elemencie nieporównywalnie szybciej niż działa taka pętla
            row = self.data_arr[i, :]
            mean = row.mean()
            std = row.std()
            if std != 0:
                self.data_arr[i, :] = (row - mean) / std
            i += 1

    # alternatywne normalizacje L2 i L1 (ponieważ, jeśli dobrze rozumiem, jest wiele sposobów normalizacji)
    def normalize_rows_l2(self):
        self.data_exists()
        self.data_arr = self.data_arr / np.linalg.norm(self.data_arr, ord=2, axis=1, keepdims=True)

    def normalize_rows_l1(self):    # DRY - wystarczyłoby przyjąć parametr ord, mógłby być z wartością domyślną
        self.data_exists()
        self.data_arr = self.data_arr / np.linalg.norm(self.data_arr, ord=1, axis=1, keepdims=True)

    def center_column(self, col_number):
        self.data_exists()
        return self.data_arr[:, col_number] - self.data_arr[:, col_number].mean()

    # def center_rows(self):  # niekoniecznie potrzebne
    #     self.data_exists()
    #     i = 0
    #     while i < self.data_arr.shape[0]:
    #         a = self.data_arr.shape[1]
    #         print(a)
    #         self.data_arr[i, :] = self.data_arr[i, :] - self.data_arr[i, :].mean()
    #         i += 1

    def data_exists(self):
        if self.data_arr is None:
            raise ValueError('No data given. Execute "read_data" first.')
