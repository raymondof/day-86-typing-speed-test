import time
import tkinter
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Typing speed test")
root.geometry("430x275")

# Create a frame within the main window
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, padx=10, pady=10)

# Set text field
text_field = Text(mainframe, width=50, height=12)#, padx=20)
text_field.grid(column=0, row=1, columnspan=4)

# Set time value and IntVar for displaying the time
time_value = 6
time_left = IntVar(mainframe)
time_left.set(time_value)
current_countdown = None

# Words Per Minute
WPM = IntVar()
WPM.set(0)

# Characters Per Minute
CPM = IntVar()
CPM.set(0)

# Variable to keep track if the user is typing in the text field
typing = False


def reset_timer():
    global typing, current_countdown
    time_left.set(time_value)

    text_field["state"] = 'normal'
    text_field.delete("1.0", "end")
    typing = False
    if current_countdown != None:
        mainframe.after_cancel(current_countdown)
        current_countdown = None


def countdown(count):
    global current_countdown
    if count > -1:
        time_left.set(count)
        current_countdown = mainframe.after(1000, countdown, count-1)
        count_words()
    if count == 0:
        text_field["state"] = 'disabled'


def start_timer():
    if current_countdown:
        # if countdown already running, cancel it
        mainframe.after_cancel(current_countdown)

    time_left.set(time_value)
    countdown(time_left.get())


def on_typing(event):
    global typing
    #if text_field.get("1.0", "end") and not current_countdown:
    if not current_countdown:
        typing = True
        start_timer()
    else:
        typing = False


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


# Bind events to the text_field
text_field.bind("<KeyRelease>", on_typing)
#text_field.bind("<KeyRelease>", start_timer)


root.mainloop()
