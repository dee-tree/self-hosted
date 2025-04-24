# Ports description

## Security

- In docker, avoid ports forwarding as it leak through system iptable and `ufw` blocks do not influence docker. Or try to map only for localhost such as: `- "127.0.0.1:80:80"`

## Services

### Public ports

- 443
- 80 (always redirects to 443!)

### Locally-mapped docker container ports (or for reverse proxy)

- 50101 (xray)
- 50102 (baikal)
- 50103 (obsidian-livesync)
- 50104 (linkwarden)
- 50105 (seafile)
- 50106 (hemmelig)
- 50107 (homebox)
- 50108 (paperless-ngx)
- 50110 (kopia)
- 50111 (portainer)
- 50112 (grafana)
- 50113 (prometheus)
- 50114 (node-exporter)

### Hidden docker container ports on networks

- 40102 (baikal)
- 40103 (obsidian-livesync)
- 40104 (linkwarden)
- 40105 (seafile)
- 40106 (hemmelig)
- 40107 (homebox)
- 40108 (paperless-ngx)
- 40110 (kopia)
- 40111 (portainer)
- 40112 (grafana)
- 40113 (prometheus)
- 40114 (node-exporter)
