# Distributed Consensus Engine
## Assignment
Subject: Distributed Systems
Topic: Resilient State Machine Replication using Paxos and PBFT
Roll Number: G25AI1072
Assignment 1(Q1)
---
## Project Overview

This project implements a resilient distributed consensus system capable of tolerating both crash faults and Byzantine faults.

The system operates in two modes:

### Mode A – Paxos (Crash Fault Tolerance)

* Leader Election
* Prepare Phase
* Promise Phase
* Accept Phase
* Commit after majority agreement

### Mode B – PBFT (Byzantine Fault Tolerance)

* Pre-Prepare
* Prepare
* Commit
* Byzantine node detection

The objective is to maintain a consistent replicated ledger across multiple distributed nodes despite failures and malicious behavior.

---

## Features

### Leader Election

* Heartbeat monitoring
* Automatic leader selection
* Fault recovery

### Paxos Consensus

* Majority voting
* Crash fault tolerance
* Transaction replication

### PBFT Consensus

* Byzantine fault tolerance
* Multi-phase agreement
* Secure transaction validation

### Byzantine Adversary

* Simulates malicious node behavior
* Sends conflicting transactions
* Tests PBFT resilience

### Chaos Testing

* Node failures
* Service recovery
* Network disruption simulation

---

## Technology Stack

* Python 3.11
* Flask
* Requests
* Cryptography
* Docker
* Docker Compose

---

## Project Structure

distributed-consensus-engine/
src/
* node.py
* adversary.py
* client.py
* crypto_utils.py
tests/
* chaos_test.sh
Dockerfile
docker-compose.yml
requirements.txt
README.md

---

## Installation

Install dependencies:

pip install -r requirements.txt

---

## Running Locally

Start node:

python src/node.py

Run client:

python src/client.py

---

## Docker Deployment

Build containers:

docker-compose build

Start services:

docker-compose up

Check running containers:

docker ps

---

## Chaos Testing

Run:

bash tests/chaos_test.sh

This test simulates:

* Node crashes
* Node recovery
* Fault tolerance validation

---

## Byzantine Testing

Run adversary node:

python src/adversary.py

Expected behavior:

* Fake transaction generation
* Conflicting messages
* Byzantine fault simulation

---

## Expected Results

* Successful leader election
* Paxos consensus under crash faults
* PBFT consensus under Byzantine faults
* Ledger consistency across nodes
* Recovery after node failures

---

## Conclusion

This project demonstrates the implementation of distributed consensus mechanisms using Paxos and PBFT. The system maintains consistency and fault tolerance under both crash and Byzantine failure scenarios while supporting containerized deployment and chaos testing.
