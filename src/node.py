from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

NODE_ID = os.environ.get("NODE_ID", "1")
MODE = os.environ.get("MODE", "PAXOS")

leader_id = "1"

ledger = []

@app.route("/")
def home():
    return {
        "node": NODE_ID,
        "mode": MODE,
        "leader": leader_id
    }

##################################
# Leader Election
##################################

@app.route("/heartbeat")
def heartbeat():
    return {"status": "alive"}

@app.route("/election", methods=["POST"])
def election():

    global leader_id

    data = request.json

    candidate = data["candidate"]

    if int(candidate) > int(leader_id):
        leader_id = candidate

    return {"leader": leader_id}

##################################
# Paxos
##################################

@app.route("/prepare", methods=["POST"])
def prepare():

    proposal = request.json["proposal"]

    print(f"Node {NODE_ID} PREPARE {proposal}")

    return {"promise": True}

@app.route("/accept", methods=["POST"])
def accept():

    txn = request.json["txn"]

    ledger.append(txn)
    with open("ledger.log", "a") as f:
        f.write(txn + "\n")

    print(f"Node {NODE_ID} ACCEPTED {txn}")

    return {"accepted": True}

##################################
# PBFT
##################################

@app.route("/preprepare", methods=["POST"])
def preprepare():

    txn = request.json["txn"]

    print(f"Node {NODE_ID} PRE-PREPARE {txn}")

    return {"ok": True}

@app.route("/prepare_pbft", methods=["POST"])
def prepare_pbft():

    txn = request.json["txn"]

    print(f"Node {NODE_ID} PREPARE {txn}")

    return {"ok": True}

@app.route("/commit", methods=["POST"])
def commit():

    txn = request.json["txn"]

    ledger.append(txn)
    with open("ledger.log", "a") as f:
        f.write(txn + "\n")

    print(f"Node {NODE_ID} COMMIT {txn}")

    return {"success": True}

##################################
# Transaction Endpoint
##################################

@app.route("/transaction", methods=["POST"])
def transaction():

    txn = request.json["txn"]

    ledger.append(txn)
    with open("ledger.log", "a") as f:
        f.write(txn + "\n")

    return {"status": "committed"}

@app.route("/ledger")
def get_ledger():

    return jsonify(ledger)

if __name__ == "__main__":

    port = 5000

    app.run(
        host="0.0.0.0",
        port=port
    )