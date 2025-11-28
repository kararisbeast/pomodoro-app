""" This script is responsible for user interface, buttons, and settings.   """
"""Mujtaba's script."""

from tkinter import *
#this tha window brah

window = Tk() #create window object
window.geometry("300x140")
window.title("Timer Screen")

# this is the title

statusLabel= Label(window, text="working..", font=("Arial", 11))
statusLabel.pack()

textLabel = Label(window, text="10:34", font=("Arial", 50, "bold"))
textLabel.pack()

# this is the buttons

button_frame = Frame(window)
button_frame.pack()

def startTimer():
    print("get to work BOZO!")

def stopTimer():
    print("relax, Bozo..")

startButton = Button(button_frame, text="start", command=startTimer)
startButton.grid(row=0, column=0, padx=10)

stopTimer = Button(button_frame, text="Stop", command=stopTimer)
stopTimer.grid(row=0, column=1, padx=10)

#this is the settings button

def settings():
    print("settings entered")

settingsButton = Button(window, text="⚙", font=("Segoe UI Symbol", 10, "bold"), command=settings)
settingsButton.place(relx=.97, anchor="ne")

window.mainloop() #place window on computer screen, listen for events