# 🛡️ Real-Time Intrusion Detection System with IAM Integration

> A network-based IDS built with **Snort 3**, integrated with **Identity and Access Management (IAM)** to detect attacks, identify attackers by user identity, and block them automatically.

---

## 📌 Abstract

In today's digital environment, traditional IDS solutions detect attacks based on IP addresses but fail to associate them with actual users or identities. This project implements a **real-time Intrusion Detection System using Snort 3**, integrated with a basic IAM module.

The system:
- Monitors live network traffic
- Detects malicious activities (ICMP ping attacks, port scans)
- Maps IP addresses to specific user identities via Python
- Automatically blocks malicious users using **iptables** firewall rules

Tested in a **Kali Linux** environment using simulated attacks via **Nmap**.

---

## 🎯 Objectives

1. Design and implement an IDS using Snort 3
2. Monitor network traffic in real-time
3. Detect malicious activities such as port scanning and ICMP attacks
4. Map attacker IP addresses to user identities
5. Automate responses such as blocking attackers
6. Integrate IDS with Identity and Access Management (IAM) concepts
7. Build a practical and deployable cybersecurity solution

---

## ⚠️ Problem Statement

Traditional IDS systems have several limitations:

| Limitation | This Project's Solution |
|---|---|
| Only display attacker IP addresses | Maps IPs to real user identities |
| No identity-aware detection | Python IAM module links attacks to users |
| No automated response | Auto-blocks attackers via iptables |
| Requires manual analysis | Automated detection and alerting pipeline |

---

## 🧠 Theory

### Intrusion Detection System (IDS)
An IDS monitors network traffic and detects suspicious activities. Types:
- **NIDS** (Network-based) — monitors entire network traffic ✅ *Used in this project*
- **HIDS** (Host-based) — monitors a single system

### Snort 3
Open-source IDS for real-time traffic analysis. Works by:
1. Capturing packets from the network
2. Comparing them with predefined rules
3. Generating alerts when matches are found

### Identity and Access Management (IAM)
Ensures the right users have appropriate access. In this project:
- IP address → User mapping is used
- Attacks are linked to identities
- Actions are taken based on identity

### Tools Used
- **Nmap** — Used to simulate attacks (port scanning, network discovery)
- **iptables** — Linux firewall utility to block malicious traffic

---

## 🔄 Workflow

```
Attacker Machine
      │
      ▼
Snort captures & analyzes packets
      │
      ▼
Suspicious activity detected → Alert generated
      │
      ▼
Python script reads alert file
      │
      ▼
IP mapped to user identity
      │
      ▼
iptables blocks attacker
```

---

## 💻 System Requirements

### Hardware
- Minimum 2 machines (or one system with network simulation)
- Processor: Intel i3 or higher
- RAM: 4GB or more

### Software
- Kali Linux / Ubuntu
- Snort 3
- Python 3
- Nmap
- Terminal (CLI environment)

---

## 🚀 Implementation Steps

### Step 1: Install Snort

```bash
sudo apt install snort
```

### Step 2: Check Network Configuration

```bash
ifconfig
```

Note down your network interface and IP address.
> Example output: Interface `wlan0`, IP `192.168.1.31`

### Step 3: Configure Snort

```bash
sudo nano /etc/snort/snort.lua
```

Set the following:
```lua
HOME_NET = '192.168.1.0/24'
EXTERNAL_NET = 'any'
```

- `HOME_NET` → defines your protected network
- `EXTERNAL_NET` → all outside traffic

### Step 4: Run Snort

```bash
sudo snort -c /etc/snort/snort.lua -i wlan0
```

**Expected output:**
- Rules loaded: 869
- Snort running successfully
- Packet processing started

### Step 5: Simulate Attack using Nmap

```bash
nmap -sS 192.168.1.31
```

- `-sS` → SYN scan (stealth scan)
- Sends packets to detect open ports

### Step 6: View Alerts

```bash
cat alert_fast.txt
```

**Alert types detected:**
- ICMP Ping Attack
- ARP Spoof detection

### Step 7: Python IAM Integration

Create `iam_detection.py`:

```python
# Mapping IP to user identity
users = {
    "192.168.1.31": "Abhishek"
}

# Open Snort alert file
with open("alert_fast.txt", "r") as f:
    for line in f:
        for ip in users:
            if ip in line:
                print(f"⚠️ Attack by {users[ip]} from IP {ip}")
```

Run:
```bash
sudo python3 iam_detection.py
```

**Sample output:**
```
⚠️ Attack by Abhishek from IP 192.168.1.31
⚠️ Attack by Abhishek from IP 192.168.1.31
```

### Step 8: Block the Attacker

```bash
sudo iptables -A INPUT -s 192.168.1.31 -j DROP
```

- `-A INPUT` → append rule to INPUT chain
- `-s` → source IP address
- `-j DROP` → silently drop all packets from this IP

**Effect:** All packets from the attacker are dropped. System is protected.

---

## 📁 Project Structure

```
IDS-Snort-IAM/
├── README.md
├── iam_detection.py          # Python IAM script
├── config/
│   ├── snort.lua             # Snort configuration
│   └── local.rules           # Custom Snort rules
└── docs/
    └── IDS_Project_Report.pdf
```

---

## ✅ Results

The system successfully:

- ✔️ Detected ICMP ping attacks
- ✔️ Detected ARP spoof attempts
- ✔️ Generated real-time alerts
- ✔️ Mapped IP addresses to user identities
- ✔️ Blocked attacker using firewall rules
- ✔️ Post-blocking Nmap scan showed all 1000 ports filtered (no response)

> This proves the system functions as a complete **Intrusion Prevention System (IPS)**.

---

## ⚖️ Advantages & Limitations

| Advantages | Limitations |
|---|---|
| Real-time intrusion detection | Static IP-to-user mapping |
| Automatic response system | No graphical interface |
| Identity-based attack detection | Limited scalability |
| Lightweight and efficient | Manual rule configuration required |
| Easy to implement | Works mainly in controlled environments |

---

## 📝 Conclusion

This project successfully demonstrates a **real-time IDS using Snort 3 integrated with IAM concepts**. Unlike traditional IDS systems that only detect attacks, this system:

- Identifies the **user behind the attack**
- Takes **automated action** to block the threat
- Creates a complete security pipeline using **Snort + Python + iptables**

The integration of IDS with IAM can significantly improve network security in real-world environments.

---

## 🛠️ Tech Stack

![Snort](https://img.shields.io/badge/Snort-3-red?style=flat-square)
![Python](https://img.shields.io/badge/Python-3-blue?style=flat-square)
![Linux](https://img.shields.io/badge/Kali_Linux-OS-black?style=flat-square)
![Nmap](https://img.shields.io/badge/Nmap-Scanner-green?style=flat-square)

---

## ⚠️ Disclaimer

This project is for **educational purposes only**. All attacks were simulated in a controlled, local environment. Do not use these techniques on networks you do not own or have explicit permission to test.
