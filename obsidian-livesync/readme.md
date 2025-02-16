# Obsidian-livesync

[Obsidian-livesync](https://github.com/vrtmrz/obsidian-livesync) is an obsidian plugin providing self-hosted notes synchronization mechanism.

## Setup

1. Clone sync server repo `git clone git@github.com:vrtmrz/self-hosted-livesync-server.git` (or skip this step because config is present)
2. Don't forget to set restrictive permissions for env file with secrets: `chmod 600 data/.secrets.env`
3. Reverse proxy configuration is in [nginx file](/nginx/config/conf.d/obsidian.mydomain.com.conf)

## Run

Being in *obsidian-livesync* directory, run:
`docker compose --env-file ./data/.secrets.env -f docker-compose.yml up -d`
