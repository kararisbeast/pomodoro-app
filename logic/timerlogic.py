#first push From Cole
import tkinter 

def GetTimerLength():
    #get's timer length from input, convert from min to seconds turn into integer
    minuteValue = int() # inside () put value user selects from dropbox
    secondsValue = minuteValue * 60
    pass

def GetBreakLength():
    #function to get value for break length from input
    #convert from min to sec's, turn into integer
    minuteValue = int() #inside () put value user selects from dropbox
    secondsValue = minuteValue * 60
    pass

def TimerStart():
    #function to start the timer
    pass

def TimerStop():
    #function to stop timer
    pass

timerValues = [] # 0 - 59 minutes user can select
for x in range(60):
    timerValues.append(x)

print(timerValues)
"""
timerLength = GetTimerLength() #assign timerlength to a var
breakLength = GetBreakLength() #assign breaklength to a var

#logic for if timerlength is greater than 0
if timerLength > 0:
    #keep timer running
    pass
elif timerLength == 0:
    #if timerlength is 0 stop timer
    pass
"""
    


