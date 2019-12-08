import pandas as pandas
from util import file_const


class file_util:
    def __init__(self, first_table, second_table):
        self.__first_table = first_table
        self.__second_table = second_table

    def get_first_table(self):
        return self.__first_table

    def get_first_table(self, first_table):
        self.__first_table = first_table

    def get_second_table(self):
        return self.__second_table

    def get_second_table(self, second_table):
        self.__second_table = second_table

    def get_transaction(self):
        transaction_1 = pandas.read_csv(self.__first_table)
        transaction_2 = pandas.read_csv(self.__second_table)
        transaction = pandas.concat(
            [transaction_1, transaction_2], ignore_index=True)
        return transaction
