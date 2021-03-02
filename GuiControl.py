from tkinter import *

window = Tk(className="Terminal")
window.geometry("500x500")

title = Label(window, text="Psychiatrist_Bot_")
title.pack()

input = Entry(window)
input.pack(pady=200)

window.mainloop()