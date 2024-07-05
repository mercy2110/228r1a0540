from tkinter import *
from PIL import ImageTk

window = Tk()

# Add widgets and set up your GUI here
frame = Frame(window)
frame.pack()

# Create a label widget and place it in the frame using grid geometry manager
usernameLabel = Label(frame, text="username")
usernameLabel.grid(row=0, column=0)
usernameEntry = Entry(frame,width=30)
usernameEntry.grid(row=0,column=1)

window.mainloop()