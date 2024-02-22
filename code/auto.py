from gologin_handle import AutoChrome
from time import sleep


class Browser:
    
    win = None
    version = "120.0.6099.110"
    pages = []
    
    def __init__(self, token, profile_id) -> None:
        self.win = AutoChrome(token, profile_id)
        self.win.createDriver(self.version)

    def visitAll(self, refresh_first_tab:bool):
        """Visits all pages in new tab
        """
        n = len(self.pages)
        self.win.get(self.pages[0])
        for i in range(0, n-1):
            self.win.newTab()
            self.win.get(self.pages[i+1])
            
                        
            self.win.switch(i)
            self.win.scrollDown()
            self.win.scrollUp()
            
        if refresh_first_tab:
            self.win.switch(0)
            self.win.refresh()
            
        self.win.switch(i+1)
        self.win.scrollDown()
        self.win.scrollUp()
        

    def visitAgain(self):
        """Starts from first tab and go last tab while scrolling them and refreshing next
        """
        n = len(self.win.window_handles)
        
        for i in range(0,n):
            if i<n:
                if i==n-1:
                    self.win.switch(0)
                else:
                    self.win.switch(i+1)
                self.win.refresh()
                
            self.win.switch(i)
            self.win.scrollDown()
            self.win.scrollUp()
    
    def close(self):
        self.win.close()