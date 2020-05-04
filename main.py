from Task import *
from tkinter import *
import tkinter.font as tkFont

tasks = []

def addTask():
    message = task_input.get()
    for i in range(len(tasks)):
        if (message in tasks[i].message) or message == '':
            print("ENTER A VALUE PLS")
            return
    tasks.append(Task(message, "False"))
    mylist.insert(END, " "*2 + message)
    task_input.delete(0, END)
    return

def openTaskList():
    try:
        with open('TasksList.txt', 'r') as f:
            for line in f:
                try:
                    message = line.split(':')[1]
                    is_done = line.split(':')[0]
                    mylist.insert(END, " "*2 + message)
                    tasks.append(Task(message, is_done))
                except IndexError:
                    pass
        print("Done!")
        return
    except FileNotFoundError:
        with open('TasksList.txt', 'w'):
            pass
        return

def saveTask():
    with open('TasksList.txt', 'w') as f:
        for i in range(len(tasks)):
            print("{}:{}".format(tasks[i].is_done, tasks[i].message), file=f)
    print("Saved!")
    return

def clearTask():
    tasks.clear()
    mylist.delete(0, END)
    return

def markAsDone():
    mylist.delete(ANCHOR)
    return

def printMess():
    if not not tasks:
        for i in range(len(tasks)):
            print(tasks[i].message)
        print('-'*15)
    return



# Create work window and set it to 500 x 800 px
window = Tk()
window.title("Simple To Do List")
window.geometry("517x800")
window.resizable(0, 0) # Unresizeable =))

titleFont = tkFont.Font(family="Verdana", size=30)
textFont = tkFont.Font(family="Verdana",size=10)
inputFont = tkFont.Font(family="Verdana",size=13)

title_lable = Label(window, padx=0, pady=0, text="To Do List", font=titleFont)
title_lable.place(x=145, y=0)



w = Scrollbar(window)
w.pack(side = RIGHT, fill=Y)
ww = Scrollbar(window, orient='horizontal')
ww.pack(side = BOTTOM, fill=X)
mylist = Listbox(window, width=44, height=30, yscrollcommand = w.set, bg="#1b1b2f", font=inputFont, fg="white")
mylist.place(x=5, y=50)
w.config( command = mylist.yview )
ww.config( command = mylist.xview )
openTaskList()



temp_lable = Label(window, pady=5)
temp_lable.place()

task_input = Entry(window, width=37, font=inputFont, fg="#ffffff", bg="#1b1b2f")
task_input.place(x=5, y=708)

add_task = Button(window, text="Add Task", fg="white", bg="#1f4068", font=textFont, command=lambda: addTask())
add_task.place(x=422, y=705)

save_task = Button(window, text="Save your to do list", fg="black", bg="#66ff63", font=textFont, command=lambda: saveTask())
save_task.place(x=5, y=740)

mark_as_done = Button(window, text="Mark as Done!", fg="white", bg="#1f4068", font=textFont, command=lambda: markAsDone())
mark_as_done.place(x=220, y=740)

clear_all_tasks = Button(window, text="Clear all tasks", fg="black", bg="#e43f5a", font=textFont, command=lambda: clearTask())
clear_all_tasks.place(x=392, y=740)

# printButt = Button(window, text="Print", fg="black", bg="#e43f5a", font=textFont, command=lambda: printMess())
# printButt.place(x=200, y=200)


mainloop()

saveTask()