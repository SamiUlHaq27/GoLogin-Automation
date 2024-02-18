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
        
        for i in range(0, n):
            self.win.get(self.pages[i])
            
            if refresh_first_tab and i==n-1:
                self.win.switch(0)
                self.win.refresh()
                self.win.switch(n-1)
                        
            if i+1<n:
                self.win.newTab()
                self.
            self.win.scrollDS()
            self.win.scrollUS()
        

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
            self.win.scrollDS()
            self.win.scrollUS()
    
    def close(self):
        self.win.close()