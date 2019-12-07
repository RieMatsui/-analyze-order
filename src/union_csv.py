import pandas as pandas

transaction_1 = pandas.read_csv('nock/analyze_order/src/csv/transaction_1.csv')
transaction_2 = pandas.read_csv('nock/analyze_order/src/csv/transaction_2.csv')

transaction_detail_1 = pandas.read_csv('nock/analyze_order/src/csv/transaction_1.csv')
transaction_detail_2 = pandas.read_csv('nock/analyze_order/src/csv/transaction_2.csv')

transaction = pandas.concat([transaction_1, transaction_2], ignore_index=True)
transaction_detail = pandas.concat([transaction_detail_1, transaction_detail_2], ignore_index=True)

print(transaction.head())

print(len(transaction_1))
print(len(transaction_2))
print(len(transaction))