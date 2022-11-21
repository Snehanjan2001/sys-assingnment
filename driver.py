from tkinter import *
# importing tkinter gui
import tkinter as tk
 
#creating window
window=tk.Tk()
 
#getting screen width and height of display
width= window.winfo_screenwidth()
height= window.winfo_screenheight()

#specifing the mouse color
window.config(cursor="dot blue")

#setting tkinter window size
window.geometry("%dx%d" % (width, height))
window.wm_attributes('-transparentcolor', '#ab23ff')
window.title("Driver Screen")
Label(window, text= " ", font= ('Helvetica 18'), bg= '#ab23ff').pack(ipadx= 600, ipady=700, padx= 2)

 
window.mainloop()