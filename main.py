from selenium import webdriver
from sys import platform
from selenium.webdriver.chrome.options import Options
from gologin import GoLogin
from time import sleep
# selenium 4
# from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run():
    if is_admin():
        # Code of your program here
        scrollGo()
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

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
        'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NWQxOTg4YTk5ZjliNTcxOGY1YWY5YTAiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NWQxYTE4Y2NlZTc3NjFhN2U1NzNjZWEifQ.ZI2tmmzQ4kjYCOz4gUjEbo0Wuhy9uLAVHaPMdRKZLKI',
        'profile_id': '65d1a16c8d3b1a11dbe529b6',
    })

    if platform == "linux" or platform == "linux2":
        chrome_driver_path = './chromedriver'
    elif platform == "darwin":
        chrome_driver_path = './mac/chromedriver'
    elif platform == "win32":
        chrome_driver_path = "chromedriver.exe"

    debugger_address = gl.start()
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", debugger_address)

    driver = webdriver.Chrome(options=chrome_options, service=ChromeService(ChromeDriverManager(driver_version="120").install()))
    # driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get("http://www.python.org")
    print(driver.title)
    
    driver.close()
    sleep(3)
    gl.stop()

# run()
scrollGo()