import requests
import sys

sub_list = open("wordlist.txt").read()
subdoms = sub_list.splitlines()

for subs in subdoms:
    sub_domains = f"http://{subs}.{sys.argv[1]}"
    
    try:
        requests.get(sub_domains)
    except:
        pass
    else:
        print("Valid Subdomains: ",sub_domains)