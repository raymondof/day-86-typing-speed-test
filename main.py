import time
import tkinter
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Typing speed test")
root.geometry("450x250")

# Create a frame within the main window
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, padx=10, pady=10)
time_value = 6

# Set text field
text_field = Text(mainframe, width=50, height=10)
text_field.grid(column=0, row=1, columnspan=4)

time_left = IntVar(mainframe)
time_left.set(time_value)

WPM = IntVar()
WPM.set(0)

CPM = IntVar()
CPM.set(0)

first_round = True
def reset_timer():
    time_left.set(time_value)
    text_field.delete("1.0", "end")
    #text_field.set

def countdown(count):
    if count > -1:
        time_left.set(count)
        mainframe.after(1000, countdown, count-1)
        #print(count)
        count_words()
    elif count == 0:
        text_field["state"] = "disabled"

def start_timer():
    time_left.set(time_value)
    text_field.delete("1.0", "end")
    countdown(time_left.get())


def count_words():
    text = text_field.get("1.0", "end")
    words_in_text = len(text.split(" "))
    characters_in_text = len(text)
    if words_in_text == 1:
        WPM.set(0)
        CPM.set(0)
    else:
        WPM.set(words_in_text)
        CPM.set(characters_in_text)

# Set labels
ttk.Label(mainframe, text="Time: ").grid(column=0, row=0, sticky=E, padx=10)
ttk.Label(mainframe, textvariable=time_left).grid(column=1, row=0, sticky=W)

ttk.Label(mainframe, text="WPM: ").grid(column=0, row=2, sticky=E, padx=10)
ttk.Label(mainframe, textvariable=WPM).grid(column=1, row=2, sticky=W)

ttk.Label(mainframe, text="CPM: ").grid(column=2, row=2, sticky=E, padx=10)
ttk.Label(mainframe, textvariable=CPM).grid(column=3, row=2, sticky=W)

# Set buttons
reset_button = tkinter.Button(mainframe, width=8, text="Reset timer", command=reset_timer)
reset_button.grid(column=2, row=0, sticky=W, padx=20)

start_button = tkinter.Button(mainframe, width=8, text="Start", command=start_timer)
start_button.grid(column=3, row=0, sticky=W, padx=20)



root.mainloop()
