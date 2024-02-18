from selenium import webdriver
from sys import platform
from selenium.webdriver.chrome.options import Options
from gologin import GoLogin
from time import sleep


def scroll(url : str):

    driver = webdriver.Chrome()

    driver.get(url)

    driver.implicitly_wait(10)

    last_height = driver.execute_script("return document.body.scrollHeight")
    sections = int(last_height / 10)
    remaining = last_height%10

    for i in range(0,sections):
        driver.execute_script("window.scrollBy(0,10)")
        sleep(0.05)

    driver.execute_script(f"window.scrollBy(0,{remaining})")

    sleep(1)

    driver.quit()

# scroll("https://en.wikipedia.org/wiki/Main_Page")


def scrollGo():

    gl = GoLogin({
        'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NWNjY2YxNzcxYTQyZjVlMjUxYzJmNDkiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NWQwYTc0MjhkM2IxYTExZGI5ODFkNTEifQ.DDuBWRGmOuZOIx4YTzyHBtf6WdQE2dWjffLM-Ca1Lks',
        'profile_id': '65d19377d54e6ec17c82c4d1',
    })

    if platform == "linux" or platform == "linux2":
        chrome_driver_path = './chromedriver'
    elif platform == "darwin":
        chrome_driver_path = './mac/chromedriver'
    elif platform == "win32":
        chrome_driver_path = "D:/Code/Business/GoLogin Automation/chrome-headless-shell-win64/chrome-headless-shell.exe"

    debugger_address = gl.start()
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", debugger_address)

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get("http://www.python.org")
    print(driver.title)
    
    driver.close()
    sleep(3)
    gl.stop()

#sdfsdfsdf
scrollGo()