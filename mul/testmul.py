from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from gologin import GoLogin


token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NWQxOTg4YTk5ZjliNTcxOGY1YWY5YTAiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NWQxYTE4Y2NlZTc3NjFhN2U1NzNjZWEifQ.ZI2tmmzQ4kjYCOz4gUjEbo0Wuhy9uLAVHaPMdRKZLKI"
profile = "65d5ae88088602d2f8ef4e5c"

gl = GoLogin({
            'token': token,
            'profile_id': profile,
        })

gl.start()
debugger_address = gl.start()
options = Options()
drvier = webdriver.Firefox(options=options)
drvier.get("https://www.python.org/")
drvier.close()
gl.stop()