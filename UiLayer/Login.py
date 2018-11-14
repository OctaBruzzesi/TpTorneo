from tkinter import *
from BusinessLogicLayer.UserLogic import UserLogic

UL = UserLogic()
gui = Tk()
gui.geometry("400x400")

def login(event):
  """UL.login(user_entry,pass_entry)"""
  print(user_entry)
  print(pass_entry)


gui.title("Login")
user_label = Label(gui, text="username").grid(row=0, column=0)
pass_label = Label(gui, text="password").grid(row=1, column=0)
user_entry = Entry(gui).grid(row=0, column=1)
pass_entry = Entry(gui, show="*").grid(row=1, column=1)

c1 = Button(gui, text="LOGIN").grid(row=5, column=0)
gui.bind('<Button-1>',login)



gui.mainloop()


