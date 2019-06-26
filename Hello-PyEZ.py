from pprint import pprint
from jnpr.junos import Device

#funkcje nie sa identyfikowane przez to, ze one beda zaciagane dopiero na linuxie

dev = Device(host = "172.25.11.1", user = "lab", password = "lab123")
dev.open()
pprint(dev.facts)
dev.close()