from Task import *
from tkinter import *

# Create work window and set it to 500 x 800 px
window = Tk()
window.geometry("500x800")

a = Entry(window)
a.pack()
print(a.get())



window.mainloop()