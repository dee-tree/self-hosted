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
- 50107 (marzban xray)
- 50110 (kopia)
- 50111 (portainer)

### Hidden docker container ports on networks

- 40102 (baikal)
- 40103 (obsidian-livesync)
- 40104 (linkwarden)
- 40105 (seafile)
- 40106 (hemmelig)
- 40107 (marzban xray)
- 40110 (kopia)
- 40111 (portainer)
