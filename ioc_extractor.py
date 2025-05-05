import re
import sys

def extract_iocs(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Regex patterns
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    domain_pattern = r'\b(?:[a-z0-9](?:[a-z0-9\-]{0,61}[a-z0-9])?\.)+(?:[a-z]{2,})\b'
    hash_pattern = r'\b[a-fA-F0-9]{32,64}\b'

    ips = set(re.findall(ip_pattern, content))
    domains = set(re.findall(domain_pattern, content))
    hashes = set(re.findall(hash_pattern, content))

    with open('ips.txt', 'w') as f:
        f.write('\n'.join(ips))
    with open('domains.txt', 'w') as f:
        f.write('\n'.join(domains))
    with open('hashes.txt', 'w') as f:
        f.write('\n'.join(hashes))

    print(f"[+] Extracted {len(ips)} IPs, {len(domains)} domains, {len(hashes)} hashes.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ioc_extractor.py <input_file>")
        sys.exit(1)

    extract_iocs(sys.argv[1])
