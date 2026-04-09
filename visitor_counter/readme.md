# Visitor Counter

A simple Python app that counts how many times it has been launched, using a Docker named volume to persist the count across container runs.

## What It Demonstrates

- Writing a Dockerfile from scratch
- Building a custom Docker image
- Using named volumes to persist data
- Container lifecycle (runs, exits, data survives)

## Files

- `counter.py` — Python script that reads, increments, and saves a count
- `Dockerfile` — Builds the image using `python:3.11-slim`

## How to Run

### 1. Build the image

```bash
docker build -t visitor_counter .
```

### 2. Create a named volume

```bash
docker volume create counter_ex_volume
```

### 3. Run it

```bash
docker run -v counter_ex_volume:/data visitor_counter
```

Run it multiple times — the count increases each time:

```
Count: 1
Count: 2
Count: 3
```

### 4. Cleanup

```bash
docker rm $(docker ps -aq --filter ancestor=visitor_counter)
docker rmi visitor_counter
docker volume rm counter_ex_volume
```