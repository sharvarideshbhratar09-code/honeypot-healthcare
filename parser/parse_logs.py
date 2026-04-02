import json

log_file = "../logs/cowrie.json"

ips = {}
commands = []

with open(log_file) as f:
    for line in f:
        data = json.loads(line)

        if "src_ip" in data:
            ip = data["src_ip"]
            ips[ip] = ips.get(ip, 0) + 1

        if data.get("eventid")  == "cowrie.command.input":
            commands.append(data["input"])

print("\nTop Attacker IPs\n")
for ip, count in ips.items():
    print(ip, count)

print("\nCommands Executed by Attackers\n")
for cmd in commands:
    print(cmd)
