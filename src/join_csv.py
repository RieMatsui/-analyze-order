import pandas as pandas

transaction_1 = pandas.read_csv('nock/analyze_order/src/csv/transaction_1.csv')
transaction_2 = pandas.read_csv('nock/analyze_order/src/csv/transaction_2.csv')
transaction_detail_1 = pandas.read_csv(
    'nock/analyze_order/src/csv/transaction_detail_1.csv')
transaction_detail_2 = pandas.read_csv(
    'nock/analyze_order/src/csv/transaction_detail_1.csv')

transaction = pandas.concat([transaction_1, transaction_2], ignore_index=True)
transaction_detail = pandas.concat(
    [transaction_detail_1, transaction_detail_2], ignore_index=True)

join_data = pandas.merge(transaction_detail, transaction[[
                         "transaction_id", "payment_date", "customer_id"]], on="transaction_id", how="left")

print(join_data.head())
print(len(transaction_detail))
print(len(transaction))
print(len(join_data))
