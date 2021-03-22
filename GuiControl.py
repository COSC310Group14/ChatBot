# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 09:56:31 2021

@author: jkran
"""
#this will be our chat bot GUI

from tkinter import *
from main import get_response, bot_name, errorString

BG_GREY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "HELVETICA 14"
FONT_BOLD = "Helvetica 13 bold"

# this class creates the chatbot window using the tkinter library.
# it imports get_response, bot_name, errorString from main.py which processes user input and porvides a response
class ChatApplication:
    
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        
    #how we start the application
    def run(self):
        self.window.mainloop()
        
    def _setup_main_window(self):
        self.window.title("Thera-bot")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470,height=550, bg=BG_COLOR) #this is how we give our widgets different attributes
        
        #head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10) #from tkinter library
        head_label.place(relwidth=1)
        
        # tiny divider
        line = Label(self.window, width=450, bg=BG_GREY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        
        #text widget
        self.text_widget = Text(self.window, width=20, height=2, wrap=WORD,bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        #scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)#whenever we change the scrollbar it changes the y pos of text
        
        #bottom label
        bottom_label = Label(self.window, bg=BG_GREY, height=80)
        bottom_label.place(relwidth=1,rely=0.825)
        
        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50",fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus() #when we start app this entry box is already selected
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        #send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GREY, command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
        
     # user clicks enter and message is sent    
    def _on_enter_pressed(self,event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
            
     #  displays response and assigns displays the nameof the sender
    def _insert_message(self, msg, sender):
        if not msg:
            return 
        
        self.msg_entry.delete(0, END) #end constant from tkinter
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        
        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        
        self.text_widget.see(END)#so we are always able to see the last message
        
if __name__ == "__main__":
    app = ChatApplication()
    app.run()
