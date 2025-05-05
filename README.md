# IOC Extractor Tool

A lightweight Python script to extract Indicators of Compromise (IOCs) such as IP addresses, domain names, and cryptographic hashes from unstructured text files. This tool is useful for SOC analysts, incident responders, and cybersecurity researchers who frequently analyze threat intelligence reports or log data.

---

## Features

- Extracts:
  - IPv4 addresses
  - Domain names (FQDN)
  - Cryptographic hashes (MD5, SHA1, SHA256)
- Saves results into separate output files:
  - `ips.txt`
  - `domains.txt`
  - `hashes.txt`
- No external libraries required (only built-in Python modules)

---

## Getting Started

### Requirements

- Python 3.6 or higher

No third-party packages are needed.

---

## Usage

1. Place your threat report or log file as a plain text file (e.g., `sample_input.txt`).
2. Run the script using:

```bash
python ioc_extractor.py sample_input.txt
