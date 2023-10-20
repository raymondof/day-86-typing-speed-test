import tkinter
from tkinter import *
from tkinter import ttk

# Create the main Tkinter window
root = Tk()
root.title("Typing speed test")
root.geometry("430x275")

# Create a frame within the main window
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, padx=10, pady=10)

# Set text field
text_field = Text(mainframe, width=50, height=12)
text_field.grid(column=0, row=1, columnspan=4)

# Set time value and IntVar for displaying the time
time_value = 60
time_left = IntVar(mainframe)
time_left.set(time_value)

# set variable for the countdown timer that avoids starting more than 1 timer
current_countdown = None

# Words Per Minute
WPM = IntVar()
WPM.set(0)

# Characters Per Minute
CPM = IntVar()
CPM.set(0)


def reset_timer():
    """Function for resetting current timer"""
    global current_countdown
    time_left.set(time_value)

    # Normalises the text field, allowing to type or edit (delete in this case)
    text_field["state"] = 'normal'
    text_field.delete("1.0", "end")
    if current_countdown is not None:
        mainframe.after_cancel(current_countdown)
        current_countdown = None


def countdown(count):
    """Performs countdown for given time (seconds)"""
    global current_countdown
    if count > -1:
        time_left.set(count)
        current_countdown = mainframe.after(1000, countdown, count-1)
        count_words()
    # Disables the text field
    if count == 0:
        text_field["state"] = 'disabled'


def start_by_typing(event):
    """Starts countdown by typing."""
    # Starts timer in case it is not running already
    if not current_countdown:
        time_left.set(time_value)
        countdown(time_left.get())


def count_words():
    """Counts the words and characters in the text_field and updates their status in the UI."""
    text = text_field.get("1.0", "end")
    words_in_text = len(text.split(" "))
    characters_in_text = len(text)

    # otherwise starts with 1
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
text_field.bind("<KeyRelease>", start_by_typing)

root.mainloop()
