import pandas as pandas
from util import file_const


class file_data:
    def __init__(self, file_name):
        self._file_name = file_name

    def get_file_head(self):
        file_head = pandas.read_csv(self._file_name)
        return file_head.head()

    def set_file_name(self, file_name):
        self._file_name = file_name

    def get_file_name(self):
        return self._file_name

    def get_transaction(self):
        transaction_1 = pandas.read_csv(file_const.const.TRANSACTION_1)
        transaction_2 = pandas.read_csv(file_const.const.TRANSACTION_2)
        transaction = pandas.concat(
            [transaction_1, transaction_2], ignore_index=True)
        return transaction
