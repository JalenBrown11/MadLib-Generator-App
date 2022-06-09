import tkinter
from tkinter import *
from tkinter import messagebox
import story_generator as stgen


def focus_next_window(e=None):
    """ Change Window Focus """
    e.widget.tk_focusNext().focus()  # Change to next widget


def auto_story():
    """ Automatic Story generation """
    story_text.delete(1.0, tkinter.END)  # Clear previous text
    story_text.insert(tkinter.END, stgen.random_madlib())  # Generate new text


def gen_story(entries=None, user_win=None):
    """ User-inputted Story Generation """
    inp_filled = True  # Flag
    for i in range(len(entries)):
        if entries[i].get() == "":  # Checks if entries are filled
            inp_filled = False  # Change false if empty
            messagebox.showerror('Input Error',  # Popup message when no filled
                                 "Didn\'t fill out all inputs. Try again.")
            user_win.focus_set()  # Refocus on user popup window
            break
    if inp_filled:
        story_text.delete(1.0, tkinter.END)  # Clear previous text
        story_text.insert(tkinter.END, stgen.madlib(*entries))  # Generate new text
        user_win.destroy()  # Closes user popup window


def user_popup():
    """ User popup window """
    # Variables
    entries = []  # Empty Entry list
    label_text = ["Name", "Role", "Place", "Adjective", "Verb"]  # List of Label text

    """ Initialize and configure User popup window """
    user_win = Toplevel(root)
    user_win.focus_set()  # Change focus to user popup window
    user_win.title("Mad Lib Generator")  # Change window title
    user_win.geometry('300x200')  # Set window size
    user_win.configure(bg="#08090D", padx=10, pady=10)
    user_win.columnconfigure(2, weight=1)
    user_win.rowconfigure(3, weight=1)

    """ Create and Map Widgets """
    # Frame
    l_frame = Frame(user_win, bg="#08090D")
    l_frame.grid(row=1, column=0, sticky=NSEW)
    r_frame = Frame(user_win, bg="#08090D")
    r_frame.grid(row=1, column=1, columnspan=2, sticky=NSEW)

    # Label
    title = Label(user_win)
    title.config(text="Please Enter Your Story", fg="#A1A69C", bg="#343A40", font=("Arial", 10))
    title.grid(row=0, column=0, columnspan=3, sticky=NSEW)

    for i in range(5):  # Creates 5 Labels for entries with names from list items
        Label(l_frame, text=f"Enter {label_text[i]}", borderwidth=1,
              fg="#A1A69C", bg="#08090D", padx=10).pack(pady=3)

    # Entry
    for i in range(5):  # Create 5 entries for user input
        entry = Entry(r_frame)
        entry.config(fg="#A1A69C", bg="#343A40", borderwidth=2,
                     highlightbackground="#08090D", highlightthickness=2)
        entry.pack()
        entries.append(entry)  # Append to list for accessing input data

    # Button
    gen_btn = Button(user_win)  # Generate user-defined story Button
    gen_btn.config(text="Generate Story", command=lambda: gen_story(entries, user_win))
    gen_btn.grid(row=2, column=1, columnspan=2, pady=3, sticky=NS)

    """ Event Bindings """
    user_win.bind('<Return>', lambda e: gen_story(entries, user_win))  # Enter key generate user-defined story
    user_win.bind('<Escape>', lambda e: user_win.destroy())  # Esc key closes user popup window


""" Initialize and configure Tkinter window """
root = Tk()
root.title("Mad Lib Generator")  # Change window title
root.config(bg="#08090D", padx=10, pady=10)
root.columnconfigure(3, weight=1)
root.rowconfigure(2, weight=1)

""" Create and Map Widgets """
# Label
label = Label(root)  # Title Label
label.config(text="Mad Lib Generator", fg="#A1A69C", bg="#343A40", font=("Arial", 15))
label.grid(row=0, column=0, sticky=NSEW)

help_txt = f"""Shortcuts
{"-" * 50}
    [Enter] - Generate
    [Shift-Enter] - Auto-Generate
    [Esc] - Quit"""
help_label = Label(root)
help_label.config(text=help_txt, fg="#A1A69C", bg="#343A40", font=("Arial", 10),
                  anchor="n", justify="left", borderwidth=1, relief=SOLID)
help_label.grid(row=0, column=1, rowspan=3, sticky=NSEW)

# Text Box
story_text = Text(root)  # Story Text Box
story_text.config(wrap=WORD, height=5, width=75, takefocus=0, fg="#A1A69C", bg="#08090D",
                  borderwidth=0, highlightthickness=3, highlightbackground="#343A40", padx=10)
story_text.grid(row=1, column=0, sticky=NSEW)
story_text.insert(tkinter.END, "")  # Insert blank space into text box

# Frame
btn_frame = Frame(root, bg="#08090D")  # Button Frame
btn_frame.rowconfigure(3, weight=1)
btn_frame.grid(row=0, column=2, rowspan=2, sticky=NSEW, padx=5)

# Button
btn1 = Button(btn_frame, text="Generate", command=user_popup)  # User popup window Button
btn1.grid(row=0, pady=5, sticky=NSEW)

btn2 = Button(btn_frame, text="Auto-Generate", command=auto_story)  # Auto-generate story Button
btn2.grid(row=1, pady=5, sticky=NSEW)

btn3 = Button(btn_frame, text="Quit", command=root.quit)  # Quit Button
btn3.grid(row=2, pady=5, sticky=NSEW)

""" Event Bindings """
root.bind('<Tab>', focus_next_window)  # Tab key changes window focus
root.bind('<Return>', lambda e: user_popup())  # Enter key opens user popup window
root.bind('<Shift-Return>', lambda e: auto_story())  # Shift-Enter key automatically generates story
root.bind('<Escape>', lambda e: root.quit())  # Esc key closes window

# Create Event Loop
root.mainloop()
