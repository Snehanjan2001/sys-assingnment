
# Import module
from tkinter import *
 
# Create object
root = Tk()
 
# Adjust size
root.geometry("400x400")
root.config(cursor="dot blue")
def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))
# Create transparent window
root.attributes('-alpha',0.1)
root.bind('<Motion>', motion)
# Execute tkinter
root.mainloop()