# Subdomain Scanner

This is a simple Python script that can be used to scan subdomains for a specified root domain.

## How to Use

1. First, create a file named `wordlist.txt` and add your list of subdomains. Each subdomain should be on a separate line.

2. Next, you can run this script with the following command:
```bash
python3 subdomain_scanner.py example.com
```
### Requirements
This script requires the following Python libraries:
  * requests

You can install these libraries using the following command:
```bash
pip3 install requests
```

### Notes
This tool performs a simple scan for subdomains. More advanced and comprehensive scanning tools are available for in-depth analysis.
During scanning, if there are errors or exceptions, this code will silently ignore them. You can modify the code to see the details of errors or exceptions.
Do not use this code for illegal or unauthorized scanning. It should only be used for legitimate and authorized purposes.
