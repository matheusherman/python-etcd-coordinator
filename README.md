# Leader Election with etcd and Python

This is a simple Python example of distributed **leader election** using [etcd](https://etcd.io/) as a coordination service.

## 📌 About

Each candidate process attempts to become the leader by writing its name to an `etcd` key. If the key is already set, the candidate waits and watches for the current leader to finish. Once the leader stops, a new candidate can take over.

This approach is useful for distributed systems where only one process should act as leader at a time.

## 🚀 How to Run

### 1. Start etcd locally (via Docker)

```bash
docker run -d \
  -p 2379:2379 \
  --name etcd-server \
  quay.io/coreos/etcd \
  etcd -advertise-client-urls http://0.0.0.0:2379 \
       -listen-client-urls http://0.0.0.0:2379
```

### 2. Install dependencies

```python
pip install etcd3
```

### 3. Run candidate processes

You can open multiple terminals and run:

```python
python candidato.py A
python candidato.py B
python candidato.py C
```

Only one will become the leader. If you stop the leader with Ctrl+C, another will take over.

## How It Works

 - Tries to get the key "lider" from etcd.
 - If it's empty, it becomes the leader and sets the key.
 - If it's already set, it watches the key until it's deleted.
 - Uses etcd3 client for interaction.
