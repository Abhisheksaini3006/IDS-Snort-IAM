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
HOME_NET = '192.168.1.0/24'
EXTERNAL_NET = 'any'


### 3. Run Snort
```bash
sudo snort -c /etc/snort/snort.lua -i wlan0
```

### 4. Run IAM Detection Script
```bash
sudo python3 iam_detection.py
```

### 5. Block Attacker
```bash
sudo iptables -A INPUT -s <attacker-IP> -j DROP
```

## How It Works
1. Snort monitors live network traffic
2. Alerts are saved to `alert_fast.txt`
3. Python script maps attacker IPs to user identities
4. Firewall rule blocks the attacker automatically

## Tools Used
- Snort 3, Python 3, iptables, Nmap
