__author__ = 'shafi'

#!/usr/bin/python3

import http.client
import hashlib
import socket

indicators = [
                "instance-id",
                "public-ipv4",
                "public-hostname",
                "ami-id",
                "hostname",
                "placement/availability-zone",
                "instance-id",
                "instance-type",
                "ami-launch-index",
                "security-groups",
                "iam/info",
                "services/domain"
]

def getInfo(datapoint):
    conn = http.client.HTTPConnection("169.254.169.254")
    conn.request("GET","/latest/meta-data/" + datapoint)
    return conn.getresponse().read().decode()

def getSignature():
    conn = http.client.HTTPConnection("169.254.169.254")
    conn.request("GET","/latest/dynamic/instance-identity/signature")
    return hashlib.sha256(conn.getresponse().read()).hexdigest()

info = {"signature": getSignature(), "_id": socket.gethostname()}

for i in indicators:
    val = getInfo(i)
    if '<?' not in val:
        info[i] = getInfo(i)

print(info)
