import nmap

#==== FILTER FOR ALIVE HOSTS ====

def host_filter(hosts):
    alive_hosts = []
    for h in hosts:
        if h['status'] == 'up':
            alive_hosts.append(h['ip'])
    return alive_hosts

#==== SCANNING INTENSITY ====

def map_intensity(level):
    if level < 1 or level > 5:
        raise ValueError("Intensity must be between 1 and 5")
    return f"T{level-1}"

#==== PROFILE ARGUMENTS ====

def profile_check(profile):
    if profile == "fast":
        return "21,22,80,443,445,3306,3389"
    elif profile == "audit":
        return "1-1000"
    elif profile == "forensic":
        return "1-65535"
    else:
        raise ValueError("Unknown profile")

#==== MAIN SCANNING FUNCTION ====

def port_scan(target, profile, intensity):
    nm = nmap.PortScanner()
    result = {}
    for host in host_filter(target):
        timing = map_intensity(intensity)
        ports = profile_check(profile)
        nm.scan(host, ports, arguments=f"-{timing} -sT -sV")
        host_data = {}
        if "tcp" in nm[host]:
            for port, info in nm[host]["tcp"].items():

                if info["state"] == "open":
                    host_data[port] = {
                        "service": info.get("product"),
                        "version": info.get("version"),
                        "state": info.get("state")
                    }
        result[host] = host_data
    return result






