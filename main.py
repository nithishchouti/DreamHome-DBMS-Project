from tkinter import *
from tkinter.ttk import *
import os


root = Tk()
root.geometry("500x500")
root.configure(bg="#6495ed")

def propreg():
    os.system('python PropertyReg.py')

def staffreg():
    os.system('python StaffReg.py')

def branch():
    os.system('python Branch.py')

def Client():
    os.system('python Client.py')

def propv():
    os.system('python PropView.py')

def lease():
    os.system('python Lease.py')

def owner():
    os.system('python Owner.py')

def q():
    os.system('python Queries.py')

style = Style()
style.configure("Custom.TButton", borderwidth=2, relief="ridge", 
                font=("Helvetica", 18), foreground="#000080", 
                background="#ff1493")


PropertyRegistration = Button(root, text="Property Registration",style="Custom.TButton", command=propreg).grid(row = 0, column=2, padx=5, pady=5, sticky="nsew")
Owner=Button(root, text="Owner Registeration", style="Custom.TButton", command=owner).grid(row = 1, column=2, padx=5, pady=5, sticky="nsew")
StaffRegistration=Button(root, text="Staff Registeration", style="Custom.TButton",command=staffreg).grid(row = 2, column=2, padx=5, pady=5, sticky="nsew")
Branch=Button(root, text="Branch Registeration", style="Custom.TButton",command=branch).grid(row = 3, column=2, padx=5, pady=5,sticky="nsew")
ClientR=Button(root, text="Client Registeration", style="Custom.TButton", command=Client).grid(row = 4, column=2, padx=5, pady=5, sticky="nsew")
PropV=Button(root, text="Property Viewing", style="Custom.TButton", command=propv).grid(row = 5, column=2, padx=5, pady=5, sticky="nsew")
Lease=Button(root, text="Lease Agreement",style="Custom.TButton", command=lease).grid(row = 6, column=2, padx=5, pady=5, sticky="nsew")
Queries=Button(root, text= "Queries", style="Custom.TButton", command=q).grid(row = 7, column=2, padx=5, pady=5, sticky="nsew")

root.mainloop()