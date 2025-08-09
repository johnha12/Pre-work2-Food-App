import http.client

conn = http.client.HTTPSConnection("")

payload = "grant_type=client_credentials&scope=basic&client_id=4916166d9569441a8e78ed58edea3ab3&client_secret=3bfbb333c5c9449899384881f8f34b4c"

headers = { 'content-type': "application/x-www-form-urlencoded" }

conn.request("POST", "https://oauth.fatsecret.com/connect/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))