import json

#==== NDB CVE JSON PARSE FOR VULNS ====

def find_cve(product, version, file):
    with open(file) as f:
        cve_db = json.load(f)
    vulnerabilities = cve_db["vulnerabilities"]
    results = []
    for item in vulnerabilities:
        configs = item["cve"].get("configurations", [])
        for config in configs:
            for node in config.get("nodes", []):
                for match in node.get("cpeMatch", []):
                    cpe = match.get("criteria", "")
                    if product in cpe and version in cpe:
                        results.append({
                            "cve": item["cve"]["id"],
                            "severity": item["cve"]["metrics"]
                        })
    return results

#==== NMAP RESULT NORMALIZER ====

def normalize(product, version):
    product = product.lower()
    parts = version.split(".")
    version = ".".join(parts[:2])
    return product, version

#==== CVE DB LOADER ====

def finder(product, version):
    year = 2026
    found = []
    product, version = normalize(product, version)
    print(product, version)
    while not found:
        file = f"CVE/{year}.json"
        found = find_cve(product, version, file)
        year=year-1
        if year == 2014:
            break
    return found