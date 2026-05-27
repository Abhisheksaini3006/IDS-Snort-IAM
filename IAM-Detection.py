# Mapping IP to user identity
users = {
    "192.168.56.4": "Ubuntu Machine"
}

# Open Snort alert file
with open("/home/molito/alert_fast.txt", "r") as f:
    for line in f:
        for ip in users:
            if ip in line:
                print("Attack by " + users[ip] + " from IP " + ip)
