from icmplib import ping
from icmplib import multiping

#==== PINGING ONE IP ====

def pinging_one(target):
    hosts = []
    host = ping(target, count=4, interval=0.2, privileged=False)
    if host.is_alive:
        hosts.append({
            "ip": target,
            "status": "up",
            "rtt": host.avg_rtt
        })
    else:
        hosts.append({
            "ip": target,
            "status": "down",
            "rtt": "None"
        })
    return hosts

#==== PINGING ENTIRE SUBNET ====

def pinging_subnet(targets):
    hosts = []

    responses = multiping(targets, count=2, interval=0.2, privileged=False)

    for host in responses:
        hosts.append({
            "ip": host.address,
            "status": "up" if host.is_alive else "down",
            "rtt": host.avg_rtt
        })

    return hosts
