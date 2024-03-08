import os 
import requests 
os.system ("clear")

username = "q1c"

print ("\nBasic IP Lookup Tool")

while True:
    host = input("" + username +
"@IP: ")
    response =
requests.get (f"http://ip-api.com/
csv/{host}?fields=isp, query")
print(response.text)