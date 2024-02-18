from gologin_handle import AutoChrome

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NWQxOTg4YTk5ZjliNTcxOGY1YWY5YTAiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NWQxYTE4Y2NlZTc3NjFhN2U1NzNjZWEifQ.ZI2tmmzQ4kjYCOz4gUjEbo0Wuhy9uLAVHaPMdRKZLKI'
profile_id = '65d1a16c8d3b1a11dbe529b6'
version = "120.0.6099.110"


web1 = AutoChrome(token, profile_id)
web1.createDriver(version)
web1.get("https://github.com/SergeyPirogov/webdriver_manager")
web1.scrollDS()
web1.get("https://en.wikipedia.org/wiki/Portal:Current_events")
web1.scrollDS()


web1.close()