#script runs traceroute (icmp) and nmap nse scripts (geolocation + asn lookup)

import os

dest_name = input("Destination: ")
os.system("sudo traceroute -I -A " + dest_name)
os.system("sudo nmap --traceroute -sn -PE --script traceroute-geolocation --script asn-query " + dest_name)

