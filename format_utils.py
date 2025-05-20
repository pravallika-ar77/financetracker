from config_utils import read_properties

def format_transaction_row(row, props):
    columns = ['transaction.date', 'transaction.amount', 'transaction.category', 'transaction.type', 'transaction.description']
    keys = ['date', 'amount', 'category', 'type', 'description']

    formatted = {}
    for i, key in enumerate(keys, start=1):  # skip id (index 0)
        label = props.get(f'transaction.{key}', key.capitalize())
        value = row[i]
        if key == 'category':
            # Map internal category to display name
            value = props.get(f'category.{value}', value)
        formatted[label] = value
    return formatted
