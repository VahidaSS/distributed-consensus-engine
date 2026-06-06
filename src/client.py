import requests
import time
import os

leader = os.getenv(
    "LEADER_URL",
    "http://node1:5000"
)

counter = 1

while True:

    txn = f"TXN-{counter}"

    try:

        r = requests.post(
            f"{leader}/transaction",
            json={"txn": txn}
        )

        print("Submitted:", txn)

    except Exception as e:
        print(e)

    counter += 1

    time.sleep(5)