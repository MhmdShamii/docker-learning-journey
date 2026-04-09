# Docker Commands Cheat Sheet

## Images

### Build an image from a Dockerfile
```bash
docker build [OPTIONS] PATH
```
| Flag | Description |
|------|-------------|
| `-t name:tag` | Give the image a name and optional tag (e.g., `myapp:v1`) |
| `.` | Build context — the folder Docker sends to the engine |

Example:
```bash
docker build -t my-app .
docker build -t my-app:v2 .
```

### List images
```bash
docker images
```

### Remove an image
```bash
docker rmi IMAGE
```
| Flag | Description |
|------|-------------|
| `-f` | Force remove even if a container is using it |

Example:
```bash
docker rmi my-app
docker rmi $(docker images -q)   # remove all images
```

### Pull an image from Docker Hub
```bash
docker pull IMAGE[:TAG]
```
Example:
```bash
docker pull nginx
docker pull python:3.11-slim
```

---

## Containers

### Run a container
```bash
docker run [OPTIONS] IMAGE [COMMAND]
```
| Flag | Description |
|------|-------------|
| `-d` | Run in background (detached mode) |
| `--name NAME` | Give the container a friendly name |
| `-p HOST:CONTAINER` | Map a port from your machine to the container |
| `-v VOLUME:PATH` | Mount a volume or bind mount at PATH inside container |
| `--network NAME` | Connect the container to a specific network |
| `--rm` | Automatically remove the container when it exits |
| `-it` | Interactive mode with a terminal (combine -i and -t) |
| `-e KEY=VALUE` | Set an environment variable inside the container |

Examples:
```bash
docker run -d --name web -p 8080:80 nginx
docker run -v mydata:/data alpine cat /data/file.txt
docker run --rm -it alpine sh
docker run -d --name db --network my-net -v dbdata:/var/lib/mysql mariadb
docker run -e MY_VAR=hello alpine env
```

### List containers
```bash
docker ps [OPTIONS]
```
| Flag | Description |
|------|-------------|
| (no flags) | Show only running containers |
| `-a` | Show all containers (running + stopped) |
| `-q` | Show only container IDs (useful for scripting) |

Examples:
```bash
docker ps
docker ps -a
docker ps -aq   # just IDs of all containers
```

### Stop a container
```bash
docker stop CONTAINER
```
Example:
```bash
docker stop my-web
docker stop $(docker ps -q)   # stop all running containers
```

### Start a stopped container
```bash
docker start CONTAINER
```
Example:
```bash
docker start my-web
```

### Remove a container
```bash
docker rm [OPTIONS] CONTAINER
```
| Flag | Description |
|------|-------------|
| `-f` | Force remove (even if running — stops it first) |

Examples:
```bash
docker rm my-web
docker rm -f my-web
docker rm $(docker ps -aq)   # remove all containers
```

### Execute a command inside a running container
```bash
docker exec [OPTIONS] CONTAINER COMMAND
```
| Flag | Description |
|------|-------------|
| `-it` | Interactive terminal (needed for shell access) |

Examples:
```bash
docker exec -it my-web bash       # open a bash shell inside
docker exec my-web cat /etc/hosts # run a single command
```

### View container logs
```bash
docker logs [OPTIONS] CONTAINER
```
| Flag | Description |
|------|-------------|
| `-f` | Follow logs in real time (like tail -f) |
| `--tail N` | Show only the last N lines |

Examples:
```bash
docker logs my-web
docker logs -f my-web
docker logs --tail 20 my-web
```

---

## Volumes

### Create a named volume
```bash
docker volume create VOLUME_NAME
```
Example:
```bash
docker volume create mydata
```

### List volumes
```bash
docker volume ls
```

### Inspect a volume
```bash
docker volume inspect VOLUME_NAME
```
Example:
```bash
docker volume inspect mydata
```

### Remove a volume
```bash
docker volume rm VOLUME_NAME
```
Example:
```bash
docker volume rm mydata
```

### Remove all unused volumes
```bash
docker volume prune [-f]
```
| Flag | Description |
|------|-------------|
| `-f` | Skip confirmation prompt |

### Mounting volumes when running containers
```bash
# Named volume — Docker manages storage location
docker run -v VOLUME_NAME:CONTAINER_PATH IMAGE

# Bind mount — you choose the exact host folder
docker run -v /host/path:/container/path IMAGE
```
Examples:
```bash
docker run -v mydata:/data alpine            # named volume
docker run -v /home/me/project:/app node     # bind mount
```

---

## Networks

### Create a network
```bash
docker network create NETWORK_NAME
```
Example:
```bash
docker network create my-network
```

### List networks
```bash
docker network ls
```

### Inspect a network
```bash
docker network inspect NETWORK_NAME
```
Example:
```bash
docker network inspect my-network
```

### Remove a network
```bash
docker network rm NETWORK_NAME
```
Example:
```bash
docker network rm my-network
```

### Remove all unused networks
```bash
docker network prune [-f]
```

### Connect a running container to a network
```bash
docker network connect NETWORK CONTAINER
```
Example:
```bash
docker network connect my-network my-web
```

### Disconnect a container from a network
```bash
docker network disconnect NETWORK CONTAINER
```

---

## Cleanup Commands

```bash
# Stop all running containers
docker stop $(docker ps -q)

# Remove all containers
docker rm $(docker ps -aq)

# Remove all images
docker rmi $(docker images -q)

# Remove all unused volumes
docker volume prune -f

# Remove all unused networks
docker network prune -f

# Nuclear option — remove everything unused
docker system prune -a --volumes -f
```

---

## Dockerfile Instructions

| Instruction | Description | Example |
|-------------|-------------|---------|
| `FROM` | Base image to start from | `FROM python:3.11-slim` |
| `WORKDIR` | Set working directory inside container | `WORKDIR /app` |
| `COPY` | Copy files from host to image | `COPY app.py .` |
| `RUN` | Execute a command during build | `RUN pip install flask` |
| `CMD` | Default command when container starts | `CMD ["python", "app.py"]` |
| `EXPOSE` | Document which port the app uses | `EXPOSE 5000` |
| `ENV` | Set environment variables | `ENV APP_MODE=production` |

### Dockerfile Example
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

---

## Quick Reference: Flag Combos You'll Use Often

```bash
# Web server with port mapping
docker run -d --name web -p 8080:80 nginx

# Database with volume and network
docker run -d --name db --network my-net -v dbdata:/var/lib/mysql mariadb

# Quick debug — get inside a container
docker exec -it container_name bash

# Run and auto-cleanup
docker run --rm -v mydata:/data alpine cat /data/file.txt

# Build and run custom image
docker build -t my-app .
docker run -d --name app -p 3000:3000 my-app
```