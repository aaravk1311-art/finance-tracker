from flask import Flask, render_template, request, redirect, url_for
import json,os

app = Flask(__name__)
DATA_FILE = 'data.json'


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []   # return empty list if no file exists

def save_data(transactions):
    with open(DATA_FILE, "w") as f:
        json.dump(transactions, f, indent=4)
 
        
@app.route("/",methods=["GET","POST"])
def index():
    transactions = load_data()
    
    if request.method == "POST":
        desc = request.form["description"]
        amount = float(request.form["amount"])
        type_= request.form["type"]
        transactions.append({"description":desc,"amount":amount,"type":type_})
        save_transaction_details(transactions)
        return redirect(url_for("index"))
    balance = sum(t["amount"] if t["type"]=="income" else -t["amount"] for t in transactions)
    return render_template("index.html",transactions=transactions,balance=balance)
if __name__ == "__main__":
    app.run(debug=True)
