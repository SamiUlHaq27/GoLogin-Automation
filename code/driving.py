from auto import Browser
import json

# ---------------------- Laptop
# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NWNjY2YxNzcxYTQyZjVlMjUxYzJmNDkiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NWQwYTc0MjhkM2IxYTExZGI5ODFkNTEifQ.DDuBWRGmOuZOIx4YTzyHBtf6WdQE2dWjffLM-Ca1Lks"


# profiles = [
#     "65d2f8693f4ddf9411abffcb",
#     "65d306c6acd907ce5d4a2adb",
#     ]
# ---------------------- Desktop
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NWQxOTg4YTk5ZjliNTcxOGY1YWY5YTAiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NWQxYTE4Y2NlZTc3NjFhN2U1NzNjZWEifQ.ZI2tmmzQ4kjYCOz4gUjEbo0Wuhy9uLAVHaPMdRKZLKI"
profiles = [
    "65d1a16c8d3b1a11dbe529b6",
    "65d5ae88088602d2f8ef4e5c",
]



class Main:
    
    flag = True
    
    def run(self, token, profile, pages):
        self.brw = Browser(token, profile)
        self.brw.pages = pages
        self.brw.visitAll(refresh_first_tab=True)
        while(self.flag):
            self.brw.visitAgain()
    
    def close(self):
        self.brw.close()
    
       
if __name__=="__main__":
    
    with open("code/files/Data.json",'r') as f:
        data = json.load(f)
        print("Profile to be run",data["profile"])
    
    exe = Main()
    exe.run(data["token"],data["profile"],data["pages"])

        