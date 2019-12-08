import pandas as pandas
from util import file_const

transaction_1 = pandas.read_csv(file_const.const.TRANSACTION_1)
transaction_2 = pandas.read_csv(file_const.const.TRANSACTION_2)
transaction_detail_1 = pandas.read_csv(file_const.const.TRANSACTION_DETAIL_1)
transaction_detail_2 = pandas.read_csv(file_const.const.TRANSACTION_DETAIL_2)

transaction = pandas.concat([transaction_1, transaction_2], ignore_index=True)
transaction_detail = pandas.concat(
    [transaction_detail_1, transaction_detail_2], ignore_index=True)

join_data = pandas.merge(transaction_detail, transaction[[
                         "transaction_id", "payment_date", "customer_id"]], on="transaction_id", how="left")

print(join_data.head())
print(len(transaction_detail))
print(len(transaction))
print(len(join_data))
