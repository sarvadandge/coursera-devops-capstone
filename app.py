from flask import Flask, request, jsonify
from flask_talisman import Talisman

app = Flask(__name__)
Talisman(app, force_https=False)

accounts = {}
counter = 1

@app.route("/accounts", methods=["POST"])
def create_account():
    global counter
    data = request.json
    accounts[counter] = data
    counter += 1
    return jsonify(data), 201

@app.route("/accounts", methods=["GET"])
def list_accounts():
    return jsonify(accounts)

@app.route("/accounts/<int:id>", methods=["GET"])
def get_account(id):
    return jsonify(accounts.get(id, {}))

@app.route("/accounts/<int:id>", methods=["PUT"])
def update_account(id):
    accounts[id] = request.json
    return jsonify(accounts[id])

@app.route("/accounts/<int:id>", methods=["DELETE"])
def delete_account(id):
    accounts.pop(id, None)
    return "", 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
