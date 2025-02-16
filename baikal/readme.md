# Baikal

Baikal is calendar (caldav) and contacts (cardav) server.

## Setup

1. Don't forget to set restrictive permissions for env file with secrets: `chmod 600 data/.secrets.env`
2. Reverse proxy configuration is in [nginx file](/nginx/config/conf.d/baikal.mydomain.com.conf)

## Run

Being in *baikal* directory, run:
`docker compose --env-file ./data/.secrets.env -f docker-compose.yml up -d`
