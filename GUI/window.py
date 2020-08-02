import tkinter as tk
from tkinter import *      

root = Tk()

canvas = Canvas(root)      
canvas.pack()      
img = PhotoImage(file="web/images/logo1.png")      
canvas.create_image(50,50, anchor=NW, image=img)      
mainloop()    