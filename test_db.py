from db_utils import fetch_all_transactions
from config_utils import read_properties
from format_utils import format_transaction_row

props = read_properties()
transactions = fetch_all_transactions()

for txn in transactions:
    formatted = format_transaction_row(txn, props)
    for k, v in formatted.items():
        print(f"{k}: {v}")
    print('---')
