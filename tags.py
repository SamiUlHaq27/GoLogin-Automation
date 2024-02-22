import tkinter as tk
import tkinter.font as tkFont
import os
import json
import multiprocessing

class Frontend:
    def __init__(self):
        color = "grey"
        self.win = tk.Tk()
        #setting title
        self.win.title("Gologin Automation")
        #setting window size
        width=600
        height=500
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

        self.profile_lbl=tk.Label(self.win)
        self.profile_lbl["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=13)
        self.profile_lbl["font"] = ft
        self.profile_lbl["fg"] = "black"
        self.profile_lbl["justify"] = "left"
        self.profile_lbl["text"] = "Profile ID"
        self.profile_lbl.place(x=10,y=302,width=70,height=25)
        self.profile_lbl["bg"] = color

        self.pages_lbl=tk.Label(self.win)
        self.pages_lbl["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=13)
        self.pages_lbl["font"] = ft
        self.pages_lbl["fg"] = "black"
        self.pages_lbl["justify"] = "left"
        self.pages_lbl["text"] = "Pages"
        self.pages_lbl.place(x=10,y=352,width=70,height=25)
        self.pages_lbl["bg"] = color
        
        self.token_fld=tk.Text(self.win)
        self.token_fld["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        self.token_fld["font"] = ft
        self.token_fld["fg"] = "black"
        self.token_fld["padx"] = 4
        self.token_fld["pady"] = 4
        self.token_fld.place(x=90,y=260,width=380,height=30)

        self.profile_fld=tk.Text(self.win)
        self.profile_fld["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        self.profile_fld["font"] = ft
        self.profile_fld["fg"] = "black"
        self.profile_fld["padx"] = 4
        self.profile_fld["pady"] = 4
        self.profile_fld.place(x=90,y=300,width=380,height=30)

        self.pages_fld=tk.Text(self.win)
        self.pages_fld["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.pages_fld["font"] = ft
        self.pages_fld["fg"] = "black"
        self.pages_fld["padx"] = 4
        self.pages_fld["pady"] = 4
        self.pages_fld.place(x=90,y=350,width=380,height=120)

        self.start_btn=tk.Button(self.win)
        self.start_btn["bg"] = "white"
        ft = tkFont.Font(family='Times',size=10)
        self.start_btn["font"] = ft
        self.start_btn["fg"] = "black"
        self.start_btn["justify"] = "center"
        self.start_btn["text"] = "Start"
        self.start_btn.place(x=500,y=310,width=70,height=25)
        self.start_btn["command"] = self.start_btn_command

        self.stop_btn=tk.Button(self.win)
        self.stop_btn["bg"] = "white"
        ft = tkFont.Font(family='Times',size=10)
        self.stop_btn["font"] = ft
        self.stop_btn["fg"] = "black"
        self.stop_btn["justify"] = "center"
        self.stop_btn["text"] = "Stop"
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
        mp = multiprocessing.Process(target=self.start)
        mp.start()
    
    def start(self):
        token = self.token_fld.get("1.0","end-1c")
        profile = self.profile_fld.get("1.0","end-1c")
        pages = (self.pages_fld.get("1.0","end-1c")).split("\n")
        with open("Data.json",'w') as f:
            json.dump({
                "token":token,
                "profile":profile,
                "pages":pages,
                },f, indent=2)
        os.system("python driving.py")
        self.update_window()

    def update_window(self):
        with open("log.txt",'r') as f:
            data = f.read()
        self.status_lbl["text"] += "\n" + data

    def stop_btn_command(self):
        self.exe.flag = False
        self.exe.close()
    
    def run(self):
        try:
            with open("Data.json",'r') as f:
                data = json.load(f)
            self.token_fld.insert("1.0",data["token"])
            self.profile_fld.insert("1.0",data["profile"])
            pages = data["pages"]
            res = ""
            for p in pages:
                res += p + "\n"
            self.pages_fld.insert("1.0",res)
        except:
            pass
        self.win.mainloop()
        
    def close(self):
        self.win.destroy()

