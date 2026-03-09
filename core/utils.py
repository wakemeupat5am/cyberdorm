from core.networkenum import *
from core.portenum import *
from core.vulnengine import *
from core.pdfengine import *

#==== SUBNET TO HOSTS DIVIDER ====

import ipaddress
def subnet_to_hosts(network):
    try:
        net = ipaddress.ip_network(network, strict=False)
        return [str(host) for host in net.hosts()]
    except ValueError:
        raise ValueError("Invalid subnet format")
    
#==== VULNSCRAPPER ====

def vulnscrapper(items):
    results = {}

    for ip, ports in items.items():
        results[ip] = {}

        for port, info in ports.items():
            service = info['service']
            version = info['version']

            vulns = finder(service, version)

            results[ip][port] = {
                "service": service,
                "version": version,
                "vulns": vulns
            }

    return results

#==== FINAL PIPELINE ====

def utils(target, profile, intensity):
    if "/" in target:
        hosts = subnet_to_hosts(target)
        ports = port_scan(pinging_subnet(hosts), profile, intensity)
    else:
        ports = port_scan(pinging_one(target), profile, intensity)
    results = vulnscrapper(ports)
    return results