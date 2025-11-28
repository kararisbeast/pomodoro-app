" This script is responsible for saving and loading the preferences such as, work duration, break duration, window size, and darkmode." 
" Karars Script "


import json




# This array holds the data that will be used by timerlogic.py and timerscreen.py
data = {
    "work_duration": 25,
    "break_duration": 5,
    "window_size": "500x400",
    "light_mode": True,
}




def LoadData():
    """ Loads the data array from a JSON file. """
    global data
    try:
        with open("save_file.json", "r") as f:
            data = json.load(f)
    except:
        pass  # keep default
    return data

LoadData()

def SaveData():
    """ Saves the data array to a JSON file. """
    global data
    with open("save_file.json", "w") as f:
        json.dump(data, f, indent=4)  # saves your data as JSON





# INSTRUCTIONS FOR USING DATA ARRAY IN OTHER SCRIPTS:
# 1. import storage.storage as storage
# 2. storage.LoadData()  # to load the data from the JSON file
# 3. Access the data using storage.data["work_duration"], storage.data["break_duration"], etc.
# 4. Modify the data as needed, e.g., storage.data["work_duration"] = 30
# 5. Call storage.SaveData() to save the changes back to the JSON file
