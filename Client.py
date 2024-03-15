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
        btn = tk.Button(self.root,text="Send text",command=self.sendMessage)
        self.message.grid(row=0, column=0)
        btn.grid(row=1,column=0)
        btn2 = tk.Button(self.root, text="show chat", command=self.see_chat)
        btn2.grid(row=2, column=0)
        self.root.mainloop()
        pass

    def sendMessage(self):
        url = "http://192.168.1.193:5000"
        text = self.message.get()
        value = {"Ip": self.ip, "Text": text}
        x = requests.post(url, data=value)
    
    def see_chat(self):
        url = "http://192.168.1.193:5000/chat"
        x = requests.get(url)
        text = tk.Label(self.root, text=x.text)
        text.grid(row=3, column=0)

App(ip)

"""
TO-DO list
- automate the text show
- make it preattier
- add a censur measur
"""