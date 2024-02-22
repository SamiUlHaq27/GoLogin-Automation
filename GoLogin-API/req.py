import requests
import json

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NWQ2ZDVjNGE1MTU0MWZjNzhmY2Q0YjUiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NWQ2ZDY1OGQxYzUzYzU2OGM4N2Y2NzkifQ.T5-IeztdBuR_mY5BCZuSNTk2-8vqBYHaoPM9IRIgpHE"

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