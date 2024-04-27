import requests
import customtkinter as ctk

class App():   
    def  __init__(self) -> None:
        self.root = ctk.CTk()
        ctk.set_appearance_mode("dark")
        self.root.geometry("500x300")
        self.root.title("Login")
        text = ctk.CTkLabel(self.root, text="Login")
        self.entry_user = ctk.CTkEntry(self.root)
        txt_user = ctk.CTkLabel(self.root, text="User: ")
        self.entry_psswd = ctk.CTkEntry(self.root)
        txt_psswd = ctk.CTkLabel(self.root, text="Password: ")
        btn_send = ctk.CTkButton(self.root, text="Send", command=self.send_login)
        text.grid(column=0, row=0)
        txt_user.grid(row=1, column=0)
        self.entry_user.grid(row=1, column=1)
        txt_psswd.grid(row=2, column=0)
        self.entry_psswd.grid(row=2, column=1)
        btn_send.grid(row=3, column=0)
        self.root.mainloop()
        pass

    def chat(self):
        self.root.title("Chat")
        self.message = ctk.CTkEntry(self.root)
        btn = ctk.CTkButton(self.root,text="Send text",command=self.sendMessage)
        user_text = ctk.CTkLabel(self.root, text="User:")
        message_text = ctk.CTkLabel(self.root, text="Message:")
        self.user = ctk.CTkEntry(self.root)
        self.user.grid(row=0, column=1)
        user_text.grid(row=0, column=0)
        message_text.grid(row=0,column=2)
        self.message.grid(row=0, column=3)
        btn.grid(row=1,column=0)
        btn2 = ctk.CTkButton(self.root, text="show chat", command=self.see_chat)
        btn2.grid(row=2, column=0)


    def sendMessage(self):
        url = "https://Software99.pythonanywhere.com"
        #Get the username and the message and covert it to a dictionary
        text = self.message.get()
        user = self.user.get()
        value = {"user": user, "Text": text}
        #Send the data to the url 
        requests.post(url, data=value)
    
    def see_chat(self):
        #Send a url request to the DB
        url = "https://Software99.pythonanywhere.com/chat"
        x = requests.get(url)
        #Get the text and remove unecessary stuff
        message = x.text.replace("),", "\n")
        message = message.replace("',", ":")
        message = message.replace("(", "")
        message = message.replace(")", "")
        message = message.replace("[", "")
        message = message.replace("]", "")        
        text = ctk.CTkLabel(self.root, text=message)
        text.grid(row=3, column=0)

    def send_login(self):
        url = "https://Software99.pythonanywhere.com/login"
        user = self.entry_user.get()
        psswd = self.entry_psswd.get()
        value = {"User": user, "Psswd": psswd}
        x = requests.post(url)
        print(x.status_code)
        if x.status_code == 200:
            #Remove every item on the page
            for widget in self.root.winfo_children():
                widget.destroy()
            #Start the Chat Page
            self.chat()

App()

"""
TO-DO list
- login in
"""