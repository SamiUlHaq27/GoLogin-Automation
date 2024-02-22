import requests
import json

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NWQ2ZDVjNGE1MTU0MWZjNzhmY2Q0YjUiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NWQ2ZDY1OGQxYzUzYzU2OGM4N2Y2NzkifQ.T5-IeztdBuR_mY5BCZuSNTk2-8vqBYHaoPM9IRIgpHE"

headers = {
    "Authorization":"Bearer "+token,
    "Content-Type":"application/json"
}

recommended = {
        "name": "Auto Browser",
        "notes": "",
        "browserType": "chrome",
        "os": "win",
        "startUrl": "",
        "googleServicesEnabled": False,
        "lockEnabled": False,
        "debugMode": False,
        "navigator": {
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.110 Safari/537.36",
            "resolution": "1360x768",
            "language": "en-US,en;q=0.9",
            "platform": "win64",
            "doNotTrack": False,
            "hardwareConcurrency": 0,
            "deviceMemory": 1,
            "maxTouchPoints": 0
        },
        "geoProxyInfo": {},
        "storage": {
            "local": True,
            "extensions": True,
            "bookmarks": True,
            "history": True,
            "passwords": True,
            "session": True
        },
        "proxyEnabled": True,
        "proxy": {
            "mode": "http",
            "host": "162.0.220.219",
            "port": "39005",
            "username": "abc123",
            "password": "123qweasd"
        },
        "dns": "",
        "plugins": {
            "enableVulnerable": True,
            "enableFlash": True
        },
        "timezone": {
            "enabled": True,
            "fillBasedOnIp": True,
            "timezone": ""
        },
        "audioContext": {
            "mode": "masked with noise",
            "noise": 0
        },
        "canvas": {
            "mode": "off",
            "noise": 0
        },
        "fonts": {
            "families": [
                "consolas"
            ],
            "enableMasking": False,
            "enableDomRect": False
        },
        "mediaDevices": {
            "videoInputs": 0,
            "audioInputs": 0,
            "audioOutputs": 0,
            "enableMasking": False
        },
        "webRTC": {
            "mode":"off",
            "enabled": False
        },
        "webGL": {
            "mode": "noise",
            "getClientRectsNoise": 0,
            "noise": 0
        },
        "clientRects": {
            "mode": "noise",
            "noise": 0
        },
        "webGLMetadata": {
            "mode": "mask",
            # "vendor": "string",
            # "renderer": "string"
        },
        "webglParams": [],
        # "profile": "string",
        # "googleClientId": "string",
        "updateExtensions": True,
        "chromeExtensions": [
            "fjkmabmdepjfammlpliljpnbhleegehm",
            "bppamachkoflopbagkdoflbgfjflfnfl",
            "gchcfdihakkhjgfmokemfeembfokkajj"
        ]
    }

response = requests.get(
    url="https://api.gologin.com/browser/",
    headers=headers
    # data=recommended
    )

try:
    res_json = response.json()
    print(json.dumps(res_json, indent=2))
    with open("create.json", 'w') as f:
        json.dump(res_json, f, indent=2)
except Exception as e:
    print(e)