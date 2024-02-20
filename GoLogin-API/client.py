import requests
import json

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NWNjY2YxNzcxYTQyZjVlMjUxYzJmNDkiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NWQwYTc0MjhkM2IxYTExZGI5ODFkNTEifQ.DDuBWRGmOuZOIx4YTzyHBtf6WdQE2dWjffLM-Ca1Lks"

headers = {
    "Authorization":"Bearer "+token,
    "Content-Type":"application/json"
}

response = requests.get(
    url="https://api.gologin.com/browser/v2",
    headers=headers
    )

res_json = response.json()
print(json.dumps(res_json, indent=2))
with open("profiles.json", 'w') as f:
    json.dump(res_json, f, indent=2)