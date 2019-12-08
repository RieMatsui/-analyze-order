import pandas as pandas
from util import file_const
from util import file_data

customer_master_file = file_data.file_data(file_const.const.CUSTOMER_MASTER)
print(customer_master_file.get_file_head())

item_master_file = file_data.file_data(file_const.const.ITEM_MASTER)
print(item_master_file.get_file_head())

transaction_1_file = file_data.file_data(file_const.const.TRANSACTION_1)
print(item_master_file.get_file_head())

transaction_detail_1_file = file_data.file_data(
    file_const.const.TRANSACTION_DETAIL_1)
print(transaction_detail_1_file.get_file_head())
