# IOC Extractor Tool

The IOC Extractor is a lightweight Python script designed to extract Indicators of Compromise (IOCs) such as IP addresses, domain names, and file hashes (MD5, SHA1, SHA256) from unstructured plain text files. This tool is particularly useful for SOC (Security Operations Center) analysts, threat hunters, and incident responders who need to quickly identify and isolate IOCs from threat reports or log files.

---

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Use Cases](#use-cases)
- [License](#license)

---

## Features

- Extracts the following types of IOCs from text:
  - IPv4 addresses
  - Domain names
  - Cryptographic hashes (MD5, SHA1, SHA256)
- Outputs results into separate, clean text files:
  - `ips.txt` for IP addresses
  - `domains.txt` for domain names
  - `hashes.txt` for file hashes
- Built using standard Python libraries (no third-party dependencies)
- Fast, portable, and easy to use in SOC workflows

---

## Getting Started

### Requirements

- Python 3.6 or higher
- A plain text file containing IOCs (such as a threat report, log dump, or raw feed)

### Installation

Clone the repository or download the source files:

```bash
git clone https://github.com/YOUR_USERNAME/ioc_extractor.git
cd ioc_extractor

## Usage

To run the tool, use the following command:

```bash
python ioc_extractor.py sample_input.txt

## Directory Structure
ioc_extractor/
├── ioc_extractor.py # Main script file
├── sample_input.txt # Example input file (optional)
├── ips.txt # Output file for IP addresses (generated)
├── domains.txt # Output file for domains (generated)
├── hashes.txt # Output file for hashes (generated)
└── README.md # Project documentation


## Use Cases

- Extracting key IOCs from MISP exports or threat intelligence reports
- Preprocessing data for ingestion into a SIEM
- Quickly identifying malicious elements in log files or email content
- Supporting incident response and triage efforts


