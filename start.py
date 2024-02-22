import json
import os

def start(token, profile, pages):
        with open("Data.json",'w') as f:
            json.dump({
                "token":token,
                "profile":profile,
                "pages":pages,
                },f, indent=2)
        os.system("python driving.py")