# Import libraries
from flask import Flask, render_template, request, redirect, url_for

# Instantiate Flask functionality
app = Flask(__name__)
# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]
 # Read operation
@app.route("/")
def get_transactions():
    return render_template("transactions.html", transactions=transactions)
# Create operation
@app.route("/add", methods=["POST"])
def add_transaction():
    if request.method == "POST":
        transaction = {
            'id': len(transactions) + 1,            # Generate a new ID based on the current length of the transactions list
            'date': request.form['date'],           # Get the 'date' field value from the form
            'amount': float(request.form['amount']) # Get the 'amount' field value from the form and convert it to a float
        }
        transactions.append(transaction)          # Add the new transaction to the transactions list    
    return redirect(url_for('get_transactions')) # Redirect to the main page to display the updated transactions list
# Update operation
@app.route("/edit/<int:transaction_id>", methods=["POST", "GET"])
def edit_transaction(transaction_id):
    if request.method == "POST":
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = request.form['date']           # Update the 'date' field of the transaction with the new value from the form
                transaction['amount'] = float(request.form['amount']) # Update the 'amount' field of the transaction with the new value from the form, converted to a float
                break
        return redirect(url_for('get_transactions')) # Redirect to the main page to display the updated transactions list
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            return render_template("edit.html", transaction=transaction) # Render the edit.html template, passing the transaction to be edited as a variable

    return {"message": "Transaction not found"} # Return a message if the transaction with the specified ID is not found
# Delete operation
@app.route("/delete/<int:transaction_id>", methods=["POST"])
def delete_transaction(transaction_id):
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction) # Remove the transaction from the transactions list
            break
    return redirect(url_for('get_transactions')) # Redirect to the main page to display the updated transactions list
# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)