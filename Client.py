import requests, socket
import tkinter as tk

class App():   
    def  __init__(self) -> None:
        self.root = tk.Tk()
        self.root.geometry("500x300")
        self.root.title("Chat")
        self.message = tk.Entry(self.root)
        btn = tk.Button(self.root,text="Send text",command=self.sendMessage)
        user_text = tk.Label(self.root, text="User:")
        message_text = tk.Label(self.root, text="Message:")
        self.user = tk.Entry(self.root)
        self.user.grid(row=0, column=1)
        user_text.grid(row=0, column=0)
        message_text.grid(row=0,column=2)
        self.message.grid(row=0, column=3)
        btn.grid(row=1,column=0)
        btn2 = tk.Button(self.root, text="show chat", command=self.see_chat)
        btn2.grid(row=2, column=0)
        self.root.mainloop()
        pass

    def sendMessage(self):
        url = "https://eldablo81.pythonanywhere.com"
        text = self.message.get()
        user = self.user.get()
        value = {"user": user, "Text": text}
        x = requests.post(url, data=value)
    
    def see_chat(self):
        url = "http://192.168.1.193:5000/chat"
        x = requests.get(url)
        text = tk.Label(self.root, text=x.text)
        text.grid(row=3, column=0)

App()

"""
TO-DO list
- automate the text show
- make it preattier
- add a censur measur
"""