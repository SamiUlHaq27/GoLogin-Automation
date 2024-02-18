from auto import Browser

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NWQxOTg4YTk5ZjliNTcxOGY1YWY5YTAiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NWQxYTE4Y2NlZTc3NjFhN2U1NzNjZWEifQ.ZI2tmmzQ4kjYCOz4gUjEbo0Wuhy9uLAVHaPMdRKZLKI'
profile_id = '65d1a16c8d3b1a11dbe529b6'
version = "120.0.6099.110"


pages = [
    # "http://127.0.0.1:5500/page1.html",
    # "http://127.0.0.1:5500/page2.html",
    # "http://127.0.0.1:5500/page3.html",
    # "http://127.0.0.1:5500/page4.html",
    # "http://127.0.0.1:5500/page5.html"
    "https://en.wikipedia.org/wiki/Main_Page",
    "https://en.wikipedia.org/wiki/Starfish",
    "https://en.wikipedia.org/wiki/Echinasteridae",
    "https://en.wikipedia.org/wiki/Zostera"
]

brw = Browser(token, profile_id)
brw.pages = pages
brw.visitAll(refresh_first_tab=True)
for i in range(0,5):
    brw.visitAgain()


brw.close()