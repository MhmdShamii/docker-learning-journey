# Docker Learning Journey

> From zero to containerized — learning Docker step by stepSSS.

## About

This repo documents my hands-on journey learning Docker from scratch. Each folder contains exercises and notes from a specific lesson, progressing from basic concepts to advanced multi-container setups.

## Progress

### Phase 1: Core Fundamentals ✅
- [x] What is Docker — images vs containers
- [x] Essential commands (`run`, `ps`, `stop`, `exec`, `logs`, `rm`)
- [x] Port mapping (`-p HOST:CONTAINER`)
- [x] Writing Dockerfiles (`FROM`, `WORKDIR`, `COPY`, `CMD`)

### Phase 2: Data & Storage 🔄
- [x] Volumes — persisting data across containers
- [x] `.dockerignore` and build context

### Phase 3: Multi-Container World
- [x] Docker networking
- [x] Docker Compose basics
- [ ] Docker Compose advanced (depends_on, restart, env vars, secrets)

### Phase 4: Real-World Practices
- [ ] Environment variables and secrets management
- [ ] PID 1 and process management
- [ ] Entrypoint scripts
- [ ] Dockerfile best practices (layer caching, multi-stage builds)

### Phase 5: Full Stack Project
- [ ] NGINX with TLS/SSL
- [ ] MariaDB setup
- [ ] WordPress + PHP-FPM
- [ ] Connecting the full stack
- [ ] Makefile orchestration

## Exercises

| Exercise | Lesson | Description |
|----------|--------|-------------|
| `visitor-counter/` | Volumes | Python app that counts launches using a named volume to persist data |
| `mini-web-stack/` | Networking | Two-container setup with NGINX and a content writer sharing a volume over a custom network |
## Tools

- **Docker Engine** on Linux
- **Python** for exercise scripts
- **Docker Compose** (upcoming)
