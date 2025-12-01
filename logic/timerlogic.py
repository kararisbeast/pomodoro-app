#first push From Cole
import storage.storage as storage

storage.LoadData()

workTime = storage.data["work_duration"] #amount of time to work
breakTime = storage.data["break_duration"] #amount of time for break

def TimerStart():
    #function to start the timer
    try:
        if workTime > 0:
    #keep timer running
            #print work time on screen in timer
            workTime =- 1
            
        elif workTime == 0:
    #if timerlength is 0 stop timer
            TimerStop()
            
    except:
        pass
    

def TimerStop():
    #function to stop timer
    try:
        if workTime > 0:
            storage.data["work_duration"] = workTime
        else:
            pass
    except:
        pass