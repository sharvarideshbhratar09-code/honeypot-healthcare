import json
from collections import Counter
import matplotlib.pyplot as plt

ips = []
commands = []

# Read Cowrie log file
with open("../logs/cowrie.json") as f:
    for line in f:
        log = json.loads(line)

        # Extract attacker IPs
        if "src_ip" in log:
            ips.append(log["src_ip"])

        # Extract commands used by attackers
        if log.get("eventid") == "cowrie.command.input":
            commands.append(log.get("input"))

# Show Top Attacker IPs
print("Top Attacker IPs:")
top_ips = Counter(ips).most_common(5)
for ip, count in top_ips:
    print(ip, count)

# Show Commands
print("\nCommands Executed by Attackers:")
for cmd in set(commands):
    print(cmd)

# Save report to file
with open("report.txt", "w") as f:
    f.write("Top Attacker IPs:\n")
    for ip, count in top_ips:
        f.write(f"{ip} {count}\n")

    f.write("\nCommands Executed:\n")
    for cmd in set(commands):
        f.write(f"{cmd}\n")

# Create graph
labels = [ip for ip, _ in top_ips]
values = [count for _, count in top_ips]

plt.bar(labels, values)
plt.title("Top Attacker IPs")
plt.xlabel("IP Address")
plt.ylabel("Number of Attacks")
plt.savefig("attacks.png")
plt.show()
