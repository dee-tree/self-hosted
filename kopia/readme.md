# Kopia

Kopia is a backup system.

Rclone's encrypted config is supported through `RCLONE_CONFIG_PASS` environment variable.

## Setup

1. Reverse proxy configuration is in [nginx file](/nginx/config/conf.d/kopia.mydomain.com.conf)

## Run

Being in *kopia* directory, run:
`docker compose --env-file ./config/.secrets.env -f docker-compose.yml up -d`

## References

- [Backups with Kopia via Docker](https://www.fuzzygrim.com/posts/kopia-backup)
