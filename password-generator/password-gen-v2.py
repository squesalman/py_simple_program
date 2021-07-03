import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import SimpleDialog

root = tk.Tk()
root.title("Password Generator")
root.resizable(width=True,height=True)

def password_gen():
  structure_1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  structure_2 = "abcdefghijklmnopqrstuvwxyz"
  structure_3 = "!@#$%^&*()"
  structure_4 = "0123456789"

  create_password = structure_1 + structure_2 + structure_3 + structure_4
  length = 20
  password = "".join(random.sample(create_password,length))
  tk.messagebox.showinfo('Your Password',password)


B = tk.Button(master=root, text ="Password Generator", command= password_gen)

B.pack()
root.mainloop()