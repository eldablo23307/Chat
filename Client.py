import requests, socket
import tkinter as tk


hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
class App():   
    def  __init__(self, ip) -> None:
        self.root = tk.Tk()
        self.ip = ip
        self.root.geometry("300x200")
        self.root.title("Chat")
        self.message = tk.Entry(self.root)
        btn = tk.Button(self.root,text="Send Ip",command=self.sendIp)
        self.message.grid(row=0, column=0)
        btn.grid(row=1,column=0)
        self.root.mainloop()
        pass

    def sendIp(self):
        url = "http://192.168.1.193:5000"
        text = self.message.get()
        value = {"Ip": self.ip, "Text": text}
        x = requests.post(url, data=value)
        
        

App(ip)