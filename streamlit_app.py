import streamlit as st
from db_utils import insert_transaction, fetch_all_transactions
from config_utils import read_properties
from format_utils import format_transaction_row

# Set up the page
st.title("Personal Finance Tracker")

# Load configuration mappings
props = read_properties()

# Transaction Input Form
st.subheader("Add New Transaction")

with st.form(key="transaction_form"):
    date = st.text_input("Date (YYYY-MM-DD)", value="2025-05-20")
    amount = st.number_input("Amount", min_value=0.0, value=0.0, step=0.01)
    category = st.text_input("Category (e.g., salary, food, rent)", value="salary")
    type_ = st.selectbox("Type", options=["income", "expense"])
    description = st.text_area("Description", value="")
    submit_button = st.form_submit_button(label="Add Transaction")

if submit_button:
    try:
        insert_transaction(date, amount, category, type_, description)
        st.success("Transaction added!")
    except Exception as e:
        st.error(f"Error: {e}")

# Display Transactions
st.subheader("Transactions")

transactions = fetch_all_transactions()
if transactions:
    # Format the transaction rows using your mappings
    formatted_transactions = [format_transaction_row(txn, props) for txn in transactions]

    # Display transactions as a table
    st.write(formatted_transactions)
else:
    st.info("No transactions found yet!")
