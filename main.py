from auto import Browser


token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NWNjY2YxNzcxYTQyZjVlMjUxYzJmNDkiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NWQwYTc0MjhkM2IxYTExZGI5ODFkNTEifQ.DDuBWRGmOuZOIx4YTzyHBtf6WdQE2dWjffLM-Ca1Lks"


profiles = [
    "65d2f8693f4ddf9411abffcb",
    "65d306c6acd907ce5d4a2adb",
    ]


pages = [
    "https://en.wikipedia.org/wiki/Main_Page",
    "https://en.wikipedia.org/wiki/Main_Page",
    "https://en.wikipedia.org/wiki/Main_Page",
    "https://en.wikipedia.org/wiki/Main_Page",
]

def run(tk, pf):
    brw = Browser(tk, pf)
    brw.pages = pages
    brw.visitAll(refresh_first_tab=True)
    for i in range(0,5):
        brw.visitAgain()


    brw.close()
    
    
if __name__ == '__main__':
    run(token, profiles[0])
    
