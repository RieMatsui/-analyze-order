import pandas as pandas

pandas.set_option('display.max_columns', 50)

customer_master = pandas.read_csv(
    'nock/analyze_order/src/csv/customer_master.csv')
item_master = pandas.read_csv('nock/analyze_order/src/csv/item_master.csv')
transaction_1 = pandas.read_csv('nock/analyze_order/src/csv/transaction_1.csv')
transaction_detail_1 = pandas.read_csv(
    'nock/analyze_order/src/csv/transaction_detail_1.csv')

print(customer_master.head())
print(len(customer_master))

print(item_master.head())
print(len(item_master))

print(transaction_1.head())
print(len(transaction_1))

print(transaction_detail_1.head())
print(len(transaction_1))
