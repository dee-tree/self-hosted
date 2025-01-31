# Caddy

Caddy is a reverse-proxy with SSL/TLS certificates management and auto renewal system.

All services are hidden besides reverse proxy.

In docker file it has its own network shared with services relied on caddy.

## Troubleshooting

### Network "caddy" not found

Create network explicitly: `docker network create caddy`
