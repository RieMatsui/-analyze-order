import pandas as pandas
from util import file_const
from util import file_util

transaction_data = file_util.file_util(
    file_const.const.TRANSACTION_1, file_const.const.TRANSACTION_2)
print(transaction_data.get_transaction().head())

transaction_detail_data = file_util.file_util(
    file_const.const.TRANSACTION_DETAIL_1, file_const.const.TRANSACTION_DETAIL_2)
print(transaction_detail_data.get_transaction().head())
