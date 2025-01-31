# Kopia

Kopia is a backup system.

Rclone's encrypted config is not supported by kopia now. Hopefully waiting for its support.

## Run

Being in *kopia* directory, run:
`docker compose --env-file ./data/.secrets.env -f docker-compose.yml up -d`
