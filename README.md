# IDS-Snort-IAM
# Real-Time Intrusion Detection System with IAM Integration

A network-based IDS built with Snort 3, integrated with Identity and 
Access Management (IAM) to detect attacks and identify attackers by 
user identity.

## Features
- Real-time traffic monitoring with Snort 3
- ICMP ping and port scan detection
- IP-to-user identity mapping via Python
- Automated attacker blocking using iptables

## Requirements
- Kali Linux / Ubuntu
- Snort 3
- Python 3
- Nmap (for testing)

## Setup & Usage

### 1. Install Snort
```bash
sudo apt install snort
```

### 2. Configure Snort
Edit `/etc/snort/snort.lua` and set:
