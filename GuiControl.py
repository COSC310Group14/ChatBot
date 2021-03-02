from tkinter import *

#this will be our chat bot gui

#first we create a window
window = Tk(className="Terminal")
window.geometry("500x500")
window.resizable(width=FALSE, height=FALSE)

title = Label(window, text="Psychiatrist_Bot_")
title.pack()

#create the main menu
main_menu = Menu(window)

# Create the submenu 
file_menu = Menu(window)

# Add commands to submenu
file_menu.add_command(label="New..")
file_menu.add_command(label="Save As..")
file_menu.add_command(label="Exit")
main_menu.add_cascade(label="File", menu=file_menu)
#Add the rest of the menu options to the main menu
main_menu.add_command(label="Edit")
main_menu.add_command(label="Quit")
window.config(menu=main_menu)

#create a window for the conversation and place in parent window
chatWindow = Text(window, bd=1, bg="black",  width="50", height="8", font=("Arial", 23), foreground="#00ffff")
chatWindow.place(x=6,y=6, height=385, width=370)

#create a text area for messages to be entered
messageWindow = Text(window, bd=0, bg="black",width="30", height="4", font=("Arial", 23), foreground="#00ffff")
messageWindow.place(x=128, y=400, height=88, width=260)

#create scroll and place in parent window
scrollbar = Scrollbar(window, command=chatWindow.yview, cursor="star")
scrollbar.place(x=375,y=5, height=385)

#create button to send messages
Button= Button(window, text="Send",  width="12", height=5,
                    bd=0, bg="#0080ff", activebackground="#00bfff",foreground='#ffffff',font=("Arial", 12))
Button.place(x=6, y=400, height=88)

window.mainloop()