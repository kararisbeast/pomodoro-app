#first push From Cole
import storage.storage as storage

storage.LoadData()

def TimerStart():
    #function to start the timer
    workTime = storage.data["work_duration"] #amount of time to work
    breakTime = storage.data["break_duration"] #amount of time for break

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
        if storage.data["work_duration"] > 0:
            pass
        else:
            pass
    except:
        pass
#add timerpause, timerunpause, timerrestart