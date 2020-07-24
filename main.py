from tkinter import *


def myClick():
    name = "Hello " + entry1.get()
    myLabel = Label(root, text=name)
    myLabel.pack()


# Creating the window for our application
root = Tk(className='paws')

entry1 = Entry(root, width=50, fg='Blue', bg='White', borderwidth=5)
entry1.pack()


button1 = Button(root, text="Enter pet name", command=myClick)
button1.pack()


# Creating an event loop. Makes our program run indefinitely
root.mainloop()
