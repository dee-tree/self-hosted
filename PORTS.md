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
- 50110 (kopia)

### Hidden docker container ports on networks

- 40102 (baikal)
- 40103 (obsidian-livesync)
- 40110 (kopia)
