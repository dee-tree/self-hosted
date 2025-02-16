# Kopia

Kopia is a backup system.

Rclone's encrypted config is not supported by kopia now. Hopefully waiting for its support.

## Setup

1. Reverse proxy configuration is in [nginx file](/nginx/config/conf.d/kopia.mydomain.com.conf)

## Run

Being in *kopia* directory, run:
`docker compose --env-file ./data/.secrets.env -f docker-compose.yml up -d`

## References

- [Backups with Kopia via Docker](https://www.fuzzygrim.com/posts/kopia-backup)
