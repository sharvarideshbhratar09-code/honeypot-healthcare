import json
from collections import Counter

ips = []
commands = []

with open("../logs/cowrie.json") as f:
    for line in f:
        log = json.loads(line)

        # Extract IP
        if "src_ip" in log:
            ips.append(log["src_ip"])

        # Extract commands
        if log.get("eventid") == "cowrie.command.input":
            commands.append(log.get("input"))

# Top attacker IPs
print("Top Attacker IPs:")
for ip, count in Counter(ips).most_common(5):
    print(ip, count)

# Commands used
print("\nCommands Executed by Attackers:")
for cmd in set(commands):
    print(cmd)


with open("report.txt", "w") as f:
    f.write("Top Attacker IPs:\n")
    for ip, count in Counter(ips).most_common(5):
        f.write(f"{ip} {count}\n")

    f.write("\nCommands Executed:\n")
    for cmd in set(commands):
        f.write(f"{cmd}\n")
