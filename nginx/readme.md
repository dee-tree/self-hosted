
## Setup

1. Before all, create the docker network: `docker network create revproxy`

## SSL

Automatic certificates management.

1. Initally, get certificates for interesting domains running the service and only http server for the service:
   1. `sudo certbot certonly --webroot --non-interactive --email mymail@provider.com --agree-tos --no-eff-email -d domain.com -w /path/to/domain.com`
2. Enable https service in nginx configuration.
3. Setup `cron` job daily to renew certificates (preferred random minute in hour):
   1. `sudo crontab -e`
   2. Add cron job to update certificate in random minute in hour:

      ```text
      SHELL=/bin/bash
      0 3 * * * sleep $((RANDOM*3600/32768)) && sudo letsencrypt renew --agree-tos >> /var/log/letsencrypt/renew.log
      ```

## Ports

It's important to setup firewall on the system to provide internet access only to specific ports (for example, 443 ssl specifically) and to isolate "private" ports with running services.

`sudo ufw enable` -- to enable "uncomplicated" ufw firewall
`sudo ufw allow ssh` or `sudo ufw allow 22/tcp` -- to open ssh(22) port for both ipv4 and ipv6. **Warning**: for safefy reasons, it's recommended to assign ssh another port than 22.

## Mounted data

### data/webroots/www/domain.name

This directory is used as "webroot" for each running service to allow letsencrypt to generate its files here to prove domain ownership.

Example of directory: `data/webroots/www/service.mydomain.com`
