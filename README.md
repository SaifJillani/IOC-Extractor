# IOC Extractor Tool 🔍

A simple Python script to extract Indicators of Compromise (IOCs) like IPs, domains, and hashes from plain text files.

## Features
- Extracts:
  - IPv4 addresses
  - Domain names
  - MD5 / SHA1 / SHA256 hashes
- Saves results in separate text files

## Usage
```bash
python ioc_extractor.py sample_input.txt
```

## Requirements
- Python 3.x (no external libraries required)

## Sample Output
Files:
- `ips.txt`
- `domains.txt`
- `hashes.txt`

## License
MIT
