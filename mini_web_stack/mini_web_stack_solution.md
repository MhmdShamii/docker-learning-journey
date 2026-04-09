# Mini Web Stack

A two-container setup where NGINX serves a webpage stored on a shared volume, written by a separate container. Both containers communicate over a custom Docker network.

## What It Demonstrates

- Creating and using custom Docker networks
- Sharing named volumes between multiple containers
- Port mapping to access services from the browser
- Container DNS resolution (only works for running containers)
- Producer/consumer pattern: one container writes, another serves

## Architecture

```
Browser → (port 8080) → NGINX → reads from shared volume
                                        ↑
                         Content Writer → writes to shared volume
```

## How to Run

### 1. Create the network and volume

```bash
docker network create web-network
docker volume create web-volume
```

### 2. Run the content writer

```bash
docker run -it --name content_writer --network web-network -v web-volume:/site alpine sh
```

Once inside the container, create the HTML file:

```bash
cat > /site/index.html
```

Write your HTML content, then press `Ctrl+D` to save. Type `exit` to leave.

### 3. Run the NGINX web server

```bash
docker run -d --name web_server -p 8080:80 -v web-volume:/usr/share/nginx/html --network web-network nginx:alpine
```

### 4. Visit the page

Open your browser and go to `http://localhost:8080`

## Key Lessons Learned

- All flags (`-d`, `--name`, `-p`, `-v`, `--network`) must come **before** the image name
- Docker DNS only resolves names of **running** containers
- The volume persists data independently — the content writer can exit and NGINX still serves the file
- Minimal images like `nginx:alpine` don't include tools like `ping`

## Cleanup

```bash
docker rm -f web_server content_writer
docker volume rm web-volume
docker network rm web-network
```