import dns.resolver
import argparse
import pyfiglet
import datetime
import sys

p = argparse.ArgumentParser()
p.add_argument("-u", "--url", required=True, metavar="", help="")
p.add_argument("-w", "--wordlist", required=False, metavar="", help="")
a = p.parse_args()

def resolverIP(url):
    try:
        dns_querys = dns.resolver.query(url, "A")
        for dns_query in dns_querys:
            return dns_query
    except Exception as e:
        print(f"Error: {e}")
        exit()

def main(url, wordlist):
    print(pyfiglet.figlet_format(f"{sys.argv[0]}"))
    print(f"STARTED: [ {str(datetime.datetime.now())[:-7]} ]")
    verify = "103.224.182.233"  #Put the DNS error ip here
    blue = "\033[1;94m"
    normal = "\033[0;0m"
    urlIP = resolverIP(url)
    print(f"TARGET: [ {url} => {urlIP} ]")
    if wordlist == None:
        wordlist = "wordlist.txt"
    try:
        lines = open(wordlist)
    except Exception as e:
        print(f"Error: {e}")
    
    for line in lines.readlines():
        newUrl = line.strip() + "." + url
        dns_querys = dns.resolver.query(newUrl, "A")
        for dns_query in dns_querys:
            if str(dns_query) != verify:
                print(f"\n{blue + '[+]' + normal} {newUrl} => {dns_query}")

if __name__ == "__main__":
    main(a.url, a.wordlist)
