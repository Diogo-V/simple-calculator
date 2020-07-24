from tkinter import *

global savedAddition  # Saves previously added number in memory so that it can be used when adding


def buttonClick(number):
    """
    When a button is clicked, we display the pressed button's number on the entry box.
    :param number: button number -> integer
    """
    currentValue = entry1.get()
    entry1.delete(0, END)
    entry1.insert(0, str(currentValue) + str(number))


def buttonEntryClear():
    """Clears all the info inside the entry box."""
    entry1.delete(0, END)


def buttonEntryAdd():
    global savedAddition
    savedAddition = int(entry1.get())
    entry1.delete(0, END)


def buttonEntryEqual():
    pass


# Creating the window for our application
root = Tk()
root.title('Calculator')

# Creates the box where we will put our code
entry1 = Entry(root, width=35, borderwidth=5)
entry1.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Set of buttons that represents our numbers
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: buttonClick(0))
button1 = Button(root, text="1", padx=40, pady=20, command=lambda: buttonClick(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: buttonClick(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: buttonClick(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: buttonClick(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: buttonClick(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: buttonClick(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: buttonClick(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: buttonClick(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: buttonClick(9))
buttonAdd = Button(root, text='+', padx=39, pady=20, command=lambda: buttonEntryAdd())
buttonEqual = Button(root, text='0', padx=91, pady=20, command=lambda: buttonEntryEqual())
buttonClear = Button(root, text='Clear', padx=79, pady=20, command=lambda: buttonEntryClear())

# Puts buttons on the screen
button0.grid(row=4, column=0)
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
buttonAdd.grid(row=5, column=0)
buttonEqual.grid(row=5, column=1, columnspan=2)
buttonClear.grid(row=4, column=1, columnspan=2)

# Creating an event loop. Makes our program run indefinitely
root.mainloop()
