from tkinter import *
import tkinter.font as tkFont

tasks = []

def addTask():
    message = inp.get()
    for i in range(len(tasks)):
        if (message == tasks[i] or message == ''):
            return
    tasks.append(message)
    my_list.insert(END, ' '*3 + message)
    inp.delete(0, END)
    return

def saveList():
    with open("TodoList.txt", 'w') as f:
        for i in range(len(tasks)):
            print(tasks[i], file=f)
    print("saved!!")
    return

def delAll():
    tasks.clear()
    my_list.delete(0, END)
    return

def markDone():
    value = my_list.get(my_list.curselection())[3:]
    print(value)
    if value in tasks:
        my_list.delete(ANCHOR)
        tasks.remove(value)
        return

def loadTodoList():
    # try to open file, if file does not exit, create file
    try:        
        with open("TodoList.txt", 'r') as f:
            for message in f:
                if message != '\n':
                    tasks.append(message)
                    my_list.insert(END, ' '*3 + message)
        print("File loaded!!")

    except FileNotFoundError:
        with open("TodoList.txt", 'w') as f:
            print("create new file")
            return


# Create a 500 x 800 px window
window = Tk()
window.title("Todo List")
window.geometry("517x800")
window.resizable(0, 0) # Unable to resize window

# Declare some font to use
titleFont = tkFont.Font(family="Verdana", size=30)
textFont = tkFont.Font(family="Verdana", size=10)
inpFont = tkFont.Font(family="Verdana", size=13)

titleLabel = Label(window, text="Simple To Do App", font=titleFont)
titleLabel.pack()

y_scrollbar = Scrollbar(window, orient="vertical")
y_scrollbar.pack(side=RIGHT, fill=Y)

x_scrollbar = Scrollbar(window, orient="horizontal")
x_scrollbar.pack(side=BOTTOM, fill=X)

my_list = Listbox(window, width=44, height=30, font=inpFont, xscrollcommand=x_scrollbar.set, yscrollcommand=y_scrollbar.set, bg="#36382e", fg="#ede6e3")
my_list.place(x=5, y=50)

y_scrollbar.config(command=my_list.yview)
x_scrollbar.config(command=my_list.xview)

loadTodoList()

inp = Entry(window, width=37, font=inpFont, bg="#36382e", fg="#e4e0de")
inp.place(x=5, y=695)

add_task = Button(window, text="Add Task", font=textFont, command=lambda: addTask(), bg="#5bc3eb", fg="#36382e")
add_task.place(x=422, y=692)

save_list = Button(window, text="Save your to do list", font=textFont, command=lambda: saveList(), bg="#b0eacd", fg="#36382e")
save_list.place(x=5, y=725)

del_all = Button(window, text="Delete all", font=textFont, command=lambda: delAll(), bg="#fd5e53", fg="#36382e")
del_all.place(x=200, y=725)

mark_done = Button(window, text="Done!", font=textFont, command=lambda: markDone(), bg="#21bf73", fg="#36382e")
mark_done.place(x=422, y=725)


mainloop()

# to make sure that any changes are being saved
saveList()