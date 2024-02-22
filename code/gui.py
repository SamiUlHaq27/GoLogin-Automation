import tkinter as tk
import tkinter.font as tkFont
import os
import json
from gologin_handle import create_profile

class Frontend:
    def __init__(self):
        color = "grey"
        self.win = tk.Tk()
        #setting title
        self.win.title("Gologin Automation")
        #setting window size
        width=600
        height=600
        screenwidth = self.win.winfo_screenwidth()
        screenheight = self.win.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.win.geometry(alignstr)
        self.win.resizable(width=False, height=False)
        #setting window color
        self.win.configure(bg=color)
        
        self.token_lbl=tk.Label(self.win)
        self.token_lbl["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=13)
        self.token_lbl["font"] = ft
        self.token_lbl["fg"] = "black"
        self.token_lbl["justify"] = "left"
        self.token_lbl["text"] = "Token"
        self.token_lbl.place(x=10,y=263,width=70,height=25)
        self.token_lbl["bg"] = color

        self.proxy_lbl=tk.Label(self.win)
        self.proxy_lbl["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=13)
        self.proxy_lbl["font"] = ft
        self.proxy_lbl["fg"] = "black"
        self.proxy_lbl["justify"] = "left"
        self.proxy_lbl["text"] = "Proxy"
        self.proxy_lbl.place(x=10,y=302,width=70,height=25)
        self.proxy_lbl["bg"] = color
        
        self.port_lbl=tk.Label(self.win)
        self.port_lbl["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=13)
        self.port_lbl["font"] = ft
        self.port_lbl["fg"] = "black"
        self.port_lbl["justify"] = "left"
        self.port_lbl["text"] = "Port"
        self.port_lbl.place(x=260,y=302,width=70,height=25)
        self.port_lbl["bg"] = color

        self.profile_lbl=tk.Label(self.win)
        self.profile_lbl["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=13)
        self.profile_lbl["font"] = ft
        self.profile_lbl["fg"] = "black"
        self.profile_lbl["justify"] = "left"
        self.profile_lbl["text"] = "Profile ID"
        self.profile_lbl.place(x=10,y=350,width=70,height=25)
        self.profile_lbl["bg"] = color
        
        self.pages_lbl=tk.Label(self.win)
        self.pages_lbl["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=13)
        self.pages_lbl["font"] = ft
        self.pages_lbl["fg"] = "black"
        self.pages_lbl["justify"] = "left"
        self.pages_lbl["text"] = "Pages"
        self.pages_lbl.place(x=10,y=400,width=70,height=25)
        self.pages_lbl["bg"] = color
        
        self.token_fld=tk.Text(self.win)
        self.token_fld["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        self.token_fld["font"] = ft
        self.token_fld["fg"] = "black"
        self.token_fld["padx"] = 4
        self.token_fld["pady"] = 4
        self.token_fld.place(x=90,y=260,width=380,height=30)

        self.proxy_fld=tk.Text(self.win)
        self.proxy_fld["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        self.proxy_fld["font"] = ft
        self.proxy_fld["fg"] = "black"
        self.proxy_fld["padx"] = 4
        self.proxy_fld["pady"] = 4
        self.proxy_fld.place(x=90,y=300,width=180,height=30)
        
        self.port_fld=tk.Text(self.win)
        self.port_fld["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        self.port_fld["font"] = ft
        self.port_fld["fg"] = "black"
        self.port_fld["padx"] = 4
        self.port_fld["pady"] = 4
        self.port_fld.place(x=320,y=300,width=150,height=30)

        self.profile_fld=tk.Text(self.win)
        self.profile_fld["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        self.profile_fld["font"] = ft
        self.profile_fld["fg"] = "black"
        self.profile_fld["padx"] = 4
        self.profile_fld["pady"] = 4
        self.profile_fld.place(x=90,y=350,width=380,height=30)
        
        self.pages_fld=tk.Text(self.win)
        self.pages_fld["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.pages_fld["font"] = ft
        self.pages_fld["fg"] = "black"
        self.pages_fld["padx"] = 4
        self.pages_fld["pady"] = 4
        self.pages_fld.place(x=90,y=400,width=380,height=120)

        self.start_btn=tk.Button(self.win)
        self.start_btn["bg"] = "white"
        ft = tkFont.Font(family='Times',size=10)
        self.start_btn["font"] = ft
        self.start_btn["fg"] = "black"
        self.start_btn["justify"] = "center"
        self.start_btn["text"] = "Start"
        self.start_btn.place(x=500,y=310,width=70,height=25)
        self.start_btn["command"] = self.start_btn_command
        
        self.start_new_btn=tk.Button(self.win)
        self.start_new_btn["bg"] = "white"
        ft = tkFont.Font(family='Times',size=10)
        self.start_new_btn["font"] = ft
        self.start_new_btn["fg"] = "black"
        self.start_new_btn["justify"] = "center"
        self.start_new_btn["text"] = "Create new"
        self.start_new_btn.place(x=485,y=400,width=100,height=25)
        self.start_new_btn["command"] = self.start_new_btn_command

        self.stop_btn=tk.Button(self.win)
        self.stop_btn["bg"] = "white"
        ft = tkFont.Font(family='Times',size=10)
        self.stop_btn["font"] = ft
        self.stop_btn["fg"] = "black"
        self.stop_btn["justify"] = "center"
        self.stop_btn["text"] = "Stop"
        self.stop_btn["state"] = "disable"
        self.stop_btn.place(x=500,y=340,width=70,height=25)
        self.stop_btn["command"] = self.stop_btn_command
        
        self.status_lbl=tk.Label(self.win)
        self.status_lbl["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=10)
        self.status_lbl["font"] = ft
        self.status_lbl["fg"] = "blue"
        self.status_lbl["bg"] = "black"
        self.status_lbl["justify"] = "right"
        self.status_lbl["text"] = "Token"
        self.status_lbl.place(x=29,y=30,width=540,height=200)

    def start_btn_command(self):
        try:
            # start(token,profile,pages)
            self.write_data_file()
            os.system("python code/driving.py")
            self.start_btn["state"] = "disable"
            self.stop_btn["state"] = "active"
        except Exception as e:
            print("Error: ",e)
        # mp = multiprocessing.Process(target=start, args=(token,profile,pages))
        # mp.start()
    
    def write_data_file(self):
        
        token = self.token_fld.get("1.0","end-1c")
        profile = self.profile_fld.get("1.0","end-1c")
        pages = (self.pages_fld.get("1.0","end-1c")).split("\n")
        
        try:
            proxy = self.proxy_fld.get("1.0","end-1c")
            port = int(self.port_fld.get("1.0","end-1c"))
        except Exception as e:
            proxy = ""
            port = 0
        
        with open("code/files/Data.json",'w') as f:
            json.dump({
                "token":token,
                "profile":profile,
                "pages":pages,
                "proxy":proxy,
                "port":port
                },f, indent=2)
        
    def start_new_btn_command(self):
        token = self.token_fld.get("1.0","end-1c")
        proxy = self.proxy_fld.get("1.0","end-1c")
        port = int(self.port_fld.get("1.0","end-1c"))
        try:
            pid = create_profile(token, proxy, port, "Auto1","EeEeEe")
            print(pid)
            self.profile_fld.delete("1.0","end-1c")
            self.profile_fld.insert("1.0",pid)
        except Exception as e:
            print("Error: ",e)
        
    def read_data_file(self):
        try:
            with open("code/files/Data.json",'r') as f:
                data = json.load(f)
            self.token_fld.insert("1.0",data["token"])
            self.profile_fld.insert("1.0",data["profile"])
            self.proxy_fld.insert("1.0",data["proxy"])
            self.port_fld.insert("1.0",data["port"])
            pages = data["pages"]
            res = ""
            for i in range(len(pages)):
                res += pages[i]
                if(i<len(pages)-1):
                    res += "\n"
            self.pages_fld.insert("1.0",res)
        except Exception as e:
            print(e)

    def stop_btn_command(self):
        self.start_btn["state"] = "active"
        self.stop_btn["state"] = "disable"
    
    def run(self):
        self.read_data_file()
        self.win.mainloop()
        
    def close(self):
        self.write_data_file()
        self.win.destroy()
    
    
if __name__=="__main__":
    
    screen = Frontend()
    screen.run()

