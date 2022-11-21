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


def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))



#setting tkinter window size
window.geometry("%dx%d" % (width, height))

window.wm_attributes('-topmost', True)
window.wait_visibility(window)
window.config(bg='')
window.wm_attributes('-alpha', 0)
window.wm_attributes('-transparentcolor', '#ab23ff')
window.title("Driver Screen")
# Label(window, text= " ", font= ('Helvetica 18'), bg= '#ab23ff').pack(ipadx= width, ipady=height, padx= 2)
exitbutton=Button(window,text="Exit",command=window.destroy).pack()
window.bind('<Motion>', motion)
window.mainloop()