from gologin_handle import AutoChrome

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NWQxOTg4YTk5ZjliNTcxOGY1YWY5YTAiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NWQxYTE4Y2NlZTc3NjFhN2U1NzNjZWEifQ.ZI2tmmzQ4kjYCOz4gUjEbo0Wuhy9uLAVHaPMdRKZLKI'
profile_id = '65d1a16c8d3b1a11dbe529b6'
version = "120.0.6099.110"

page1 = "http://127.0.0.1:5500/page1.html"
page2 = "http://127.0.0.1:5500/page2.html"
page3 = "http://127.0.0.1:5500/page3.html"
page4 = "http://127.0.0.1:5500/page4.html"
page5 = "http://127.0.0.1:5500/page5.html"

web1 = AutoChrome(token, profile_id)
web1.createDriver(version)
web1.get(page1)
web1.scrollDS()

web1.newTab()

web1.get(page2)
web1.scrollDS()


web1.close()