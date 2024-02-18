from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gologin import GoLogin
from time import sleep


class AutoChrome:
    
    token = None
    profile_id = None
    driver = None
    gl = None
    
    window_handles = []
    
    def __init__(self, token, profile_id) -> None:
        self.token = token
        self.profile_id = profile_id
        
    def createDriver(self, version):
        self.gl = GoLogin({
            'token': self.token,
            'profile_id': self.profile_id,
        })
        
        debugger_address = self.gl.start()
        chrome_options = Options()
        chrome_options.browser_version = version
        chrome_options.add_experimental_option("debuggerAddress", debugger_address)
        self.driver = webdriver.Chrome(options=chrome_options)
        
    def scrollDown(self):
        """Scroll down slowly
        """
        
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        sections = int(last_height / 5)
        remaining = last_height%10
        for i in range(0,sections):
            self.driver.execute_script("window.scrollBy(0,10)")
            sleep(0.03)

        self.driver.execute_script(f"window.scrollBy(0,{remaining})")
    
    def scrollUp(self):
        """Scroll Up
        """
        
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        self.driver.execute_script(f"window.scrollTo({last_height},0)")
    
    def get(self, url : str):
        self.driver.implicitly_wait(10)
        self.driver.get(url)        
        self.window_handles.append(self.driver.current_window_handle)
        # Print statement here
        print(self.driver.title, " loaded")
        
    def newTab(self):
        self.driver.switch_to.new_window('tab')
    
    def refresh(self):
        # Print statement here
        print(self.driver.title," refreshed")
        self.driver.refresh()
    
    def switch(self, ind:int):
        win_handle = self.window_handles[ind]
        self.driver.switch_to.window(win_handle)
    
    
    def close(self):
        self.driver.close()
        sleep(3)
        self.gl.stop()
        
    
    
def scrollGo():

    gl = GoLogin({
        'token': 'yJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NWQxOeTg4YTk5ZjliNTcxOGY1YWY5YTAiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NWQxYTE4Y2NlZTc3NjFhN2U1NzNjZWEifQ.ZI2tmmzQ4kjYCOz4gUjEbo0Wuhy9uLAVHaPMdRKZLKI',
        'profile_id': '65d1a16c8d3b1a11dbe529b6',
    })

    debugger_address = gl.start()
    chrome_options = Options()
    chrome_options.browser_version = "120.0.6099.110"
    chrome_options.add_experimental_option("debuggerAddress", debugger_address)

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get("http://www.python.org")
    
    last_height = driver.execute_script("return document.body.scrollHeight")
    sections = int(last_height / 10)
    remaining = last_height%10
    for i in range(0,sections):
        driver.execute_script("window.scrollBy(0,10)")
        sleep(0.05)

    driver.execute_script(f"window.scrollBy(0,{remaining})")
    
    driver.close()
    sleep(3)
    gl.stop()