import pandas as pandas
from util import file_const

customer_master = pandas.read_csv(file_const.const.CUSTOMER_MASTER)
item_master = pandas.read_csv(file_const.const.ITEM_MASTER)
transaction_1 = pandas.read_csv(file_const.const.TRANSACTION_1)
transaction_detail_1 = pandas.read_csv(file_const.const.TRANSACTION_DETAIL_1)

print(customer_master.head())
print(len(customer_master))

print(item_master.head())
print(len(item_master))

print(transaction_1.head())
print(len(transaction_1))

print(transaction_detail_1.head())
print(len(transaction_1))
