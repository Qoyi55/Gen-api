from flask import Flask, jsonify
import random

app = Flask(__name__)

def load_accounts():
    accounts = []
    with open("stocks.txt", "r") as file:
        for line in file:
            if ":" in line:
                username, password = line.strip().split(":", 1)
                accounts.append({"Username": username, "Password": password})
    return accounts

unused_accounts = load_accounts()

@app.route('/get_account', methods=['GET'])
def get_account():
    global unused_accounts
    if not unused_accounts:
        return jsonify({"error": "No more accounts available"}), 404
    selected_account = random.choice(unused_accounts)
    unused_accounts.remove(selected_account)
    return jsonify(selected_account)

if __name__ == '__main__':
    app.run(debug=True, port=5000
