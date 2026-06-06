from flask import Flask

app = Flask(__name__)

@app.route("/preprepare", methods=["POST"])
def malicious():

    print("BYZANTINE NODE")

    print("Sending conflicting transaction")

    return {
        "txn":"FAKE_TRANSACTION"
    }

@app.route("/")
def home():

    return {
        "node":"malicious"
    }

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5001
    )