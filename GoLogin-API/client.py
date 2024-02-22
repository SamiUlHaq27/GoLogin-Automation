import gologin

def create_profile(token, host, port):
    gl = gologin.GoLogin({
        "token":token
    })
    
    profile_id = gl.create()
    
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
        "platform": "string",
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
    "proxyEnabled": False,
    "proxy": {
        "mode": "http",
        "host": "string",
        "port": 0,
        "username": "string",
        "password": "string"
    },
    "dns": "string",
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
        "mode": "off",
        "noise": 0
    },
    "canvas": {
        "mode": "off",
        "noise": 0
    },
    "fonts": {
        "families": [
            "string"
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
        "mode": "alerted",
        "enabled": True,
        "customize": True,
        "localIpMasking": False,
        "fillBasedOnIp": True,
        "publicIp": "string",
        "localIps": [
            "string"
        ]
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
        "vendor": "string",
        "renderer": "string"
    },
    "webglParams": [],
    "profile": "string",
    "googleClientId": "string",
    "updateExtensions": True,
    "chromeExtensions": [
        "string"
    ]
}