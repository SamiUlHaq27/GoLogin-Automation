import requests
import json

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NWQxOTg4YTk5ZjliNTcxOGY1YWY5YTAiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NWQxYTE4Y2NlZTc3NjFhN2U1NzNjZWEifQ.ZI2tmmzQ4kjYCOz4gUjEbo0Wuhy9uLAVHaPMdRKZLKI"

headers = {
    "Authorization":"Bearer "+token,
    "Content-Type":"application/json"
}

response = requests.get(
    url="https://api.gologin.com/browser/v2",
    headers=headers
    )

res_json = response.json()
with open("profiles.json", 'w') as f:
    json.dump(res_json, f, indent=2)