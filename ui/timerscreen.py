""" This script is responsible for user interface, buttons, and settings.   """
"""Mujtaba's script."""

from tkinter import *

#this tha window brah

window = Tk() #create window object
window.geometry("300x140")
window.title("Timer Screen")

# frames
main_frame=Frame(window)
settings_frame=Frame(window)

main_frame.pack(fill="both", expand=True)

# main screen

statusLabel= Label(main_frame, text="working..", font=("Arial", 11))
statusLabel.pack()

textLabel = Label(main_frame, text="10:34", font=("Arial", 50, "bold"))
textLabel.pack()

button_frame = Frame(main_frame)
button_frame.pack()

def startTimer():
    print("get to work BOZO!")

def stopTimer():
    print("relax, Bozo..")

startButton = Button(button_frame, text="start", command=startTimer)
startButton.grid(row=0, column=0, padx=10)

stopTimer = Button(button_frame, text="Stop", command=stopTimer)
stopTimer.grid(row=0, column=1, padx=10)

# the switch to settings
def settings():
    main_frame.pack_forget()
    settings_frame.pack(fill="both", expand=True)

def go_back():
    settings_frame.pack_forget()
    main_frame.pack(fill="both", expand=True)

#prevent widget duplication
for widget in settings_frame.winfo_children():
    widget.destroy()

#new widgets
Label(settings_frame, text = "Settings Menu", font=("Arial", 12, "bold")).pack(pady=10)
Button(settings_frame, text="back", command=go_back).pack(pady=5)


settingsButton = Button(window, text="⚙", font=("Segoe UI Symbol", 10, "bold"), command=settings)
settingsButton.place(relx=.97, anchor="ne")


window.mainloop() #place window on computer screen, listen for events