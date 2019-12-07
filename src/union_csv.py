import pandas as pandas
from util import file_const

transaction_1 = pandas.read_csv(file_const.const.TRANSACTION_1)
transaction_2 = pandas.read_csv(file_const.const.TRANSACTION_2)

transaction_detail_1 = pandas.read_csv(file_const.const.TRANSACTION_DETAIL_1)
transaction_detail_2 = pandas.read_csv(file_const.const.TRANSACTION_DETAIL_2)

transaction = pandas.concat([transaction_1, transaction_2], ignore_index=True)
transaction_detail = pandas.concat([transaction_detail_1, transaction_detail_2], ignore_index=True)

print(transaction.head())

print(len(transaction_1))
print(len(transaction_2))
print(len(transaction))