import glob
import pyautogui
import tkinter as tk
from time import sleep

global stringSelect
global stringBan
stringSelect = [""]
stringBan = [""]

global searchBoxXY
global aboveChampXY
searchBoxXY = None
aboveChampXY = None

def accept():
    if buttonAccept.config('text')[-1] == "Enabled":
        print("Queuing!")
        acceptXY = None
        for pngName in glob.iglob("accept/*"):
            if acceptXY == None:
                acceptXY = pyautogui.locateCenterOnScreen(pngName, confidence = 0.6)
            else:
                print("Found accept!")
                break
            
        if acceptXY != None:
            buttonAccept.config(text = "Disabled")
            pyautogui.click(acceptXY, duration = 0.5)
            sleep(13)
            print("Done waiting!")
            inQueue = pyautogui.locateCenterOnScreen("greyInQueue.png", confidence = 0.6)
            inQueueDark = pyautogui.locateCenterOnScreen("greyInQueueDark.png", confidence = 0.6)
            if inQueue != None or inQueueDark != None:
                buttonAccept.config(text = "Enabled")
            else:
                global searchBoxXY
                for pngName in glob.iglob("searchBox/*"):
                    if searchBoxXY == None:
                        searchBoxXY = pyautogui.locateCenterOnScreen(pngName, confidence = 0.6)
                    else:
                        print("Found search!")
                        break

                global aboveChampXY
                for pngName in glob.iglob("aboveChamp/*"):
                    if aboveChampXY == None:
                        aboveChampXY = pyautogui.locateCenterOnScreen(pngName, confidence = 0.6)
                    else:
                        print("Found champ!")
                        break
        root.after(2000, accept)

def select():
    try:
        if buttonSelect.config('text')[-1] == "Enabled":
            selecting = None
            for pngName in glob.iglob("selecting/*"):
                if selecting == None:
                    selecting = pyautogui.locateCenterOnScreen(pngName, confidence = 0.6)
                else:
                    print("In select phase!")
                    break
            if selecting != None:
                print("Selecting!")
                selected = False
                stringSelect = entrySelect.get().lower().split(', ')
                for line in stringSelect:
                    print(line)
                if stringSelect[0] == "":
                    buttonSelect.config(text = "Disabled")
                    pyautogui.alert("Please input a champion name.")
                else:
                    greyLockInXY = None
                    for pngName in glob.iglob("greyLockIn/*"):
                        if greyLockInXY == None:
                            greyLockInXY = pyautogui.locateCenterOnScreen(pngName, confidence = 0.6)
                        else:
                            print("Found greyLockIn!")
                            break

                    global searchBoxXY
                    for pngName in glob.iglob("searchBox/*"):
                        if searchBoxXY == None:
                            searchBoxXY = pyautogui.locateCenterOnScreen(pngName, confidence = 0.6)
                        else:
                            print("Found search!")
                            break

                    global aboveChampXY
                    for pngName in glob.iglob("aboveChamp/*"):
                        if aboveChampXY == None:
                            aboveChampXY = pyautogui.locateCenterOnScreen(pngName, confidence = 0.6)
                        else:
                            print("Found champ!")
                            break

                    if greyLockInXY != None and searchBoxXY != None and aboveChampXY != None:
                        sIter = iter(stringSelect)
                        while True:
                            name = next(sIter, "None")
                            if selected == False and name == "None":
                                pyautogui.alert("Champion(s) not available. Please enter a new one.")
                                break
                            if name == "None":
                                break
                            buttonSelect.config(text = "Disabled")
                            pyautogui.click(searchBoxXY, duration = 0.5)
                            pyautogui.hotkey('ctrl', 'a')
                            pyautogui.press('backspace')
                            sleep(1)
                            pyautogui.typewrite(name, interval = 0.25)
                            pyautogui.click(aboveChampXY.x - 65, aboveChampXY.y + 65, duration = 0.5)
                            lockInXY = None
                            for pngName in glob.iglob("lockIn/*"):
                                if lockInXY == None:
                                    lockInXY = pyautogui.locateCenterOnScreen(pngName, confidence = 0.6)
                                else:
                                    print("Locked in champ!")
                                    pyautogui.click(lockInXY, duration = 0.5)
                                    selected = True
                                    break
            root.after(2000, select)
    except:
        buttonSelect.config(text = "Disabled")
        pyautogui.alert("An error occurred. Please retry the program.")

def ban():
    try:
        if buttonBan.config('text')[-1] == "Enabled":
            banning = None
            for pngName in glob.iglob("banning/*"):
                if banning == None:
                    banning = pyautogui.locateCenterOnScreen(pngName, confidence = 0.6)
                else:
                    print("In ban phase!")
                    break
            if banning != None:
                print("Banning!")
                banned = False
                stringBan = entryBan.get().lower().split(', ')
                for line in stringBan:
                    print(line)
                if stringBan[0] == "":
                    buttonBan.config(text = "Disabled")
                    pyautogui.alert("Please input a champion name.")
                else:
                    greyBanXY = None
                    for pngName in glob.iglob("greyBan/*"):
                        if greyBanXY == None:\
                            greyBanXY = pyautogui.locateCenterOnScreen(pngName, confidence = 0.6)
                        else:
                            print("Found greyBan!")
                            break
                    global searchBoxXY
                    for pngName in glob.iglob("searchBox/*"):
                        if searchBoxXY == None:
                            searchBoxXY = pyautogui.locateCenterOnScreen(pngName, confidence = 0.6)
                        else:
                            print("Found search!")
                            break
                    global aboveChampXY
                    for pngName in glob.iglob("aboveChamp/*"):
                        if aboveChampXY == None:
                            aboveChampXY = pyautogui.locateCenterOnScreen(pngName, confidence = 0.6)
                        else:
                            print("Found champ!")
                            break
                    if greyBanXY != None and searchBoxXY != None and aboveChampXY != None:
                        sIter = iter(stringBan)
                        while True:
                            name = next(sIter, "None")
                            if banned == False and name == "None":
                                pyautogui.alert("Champion(s) not available. Please enter a new one.")
                                break
                            if name == "None":
                                break
                            buttonBan.config(text = "Disabled")
                            pyautogui.click(searchBoxXY, duration = 0.5)
                            pyautogui.hotkey('ctrl', 'a')
                            pyautogui.press('backspace')
                            sleep(1)
                            pyautogui.typewrite(name, interval = 0.25)
                            pyautogui.click(aboveChampXY.x - 65, aboveChampXY.y + 65, duration = 0.5)
                            banXY = None
                            for pngName in glob.iglob("ban/*"):
                                if banXY == None:
                                    banXY = pyautogui.locateCenterOnScreen(pngName, confidence = 0.6)
                                else:
                                    print("Locked in ban!")
                                    pyautogui.click(banXY, duration = 0.5)
                                    banned = True
                                    break
            root.after(2000, ban)
    except:
        buttonBan.config(text = "Disabled")
        pyautogui.alert("An error occurred. Please retry the program.")

# Button togglers
def toggleAcceptButton():
    if buttonAccept.config("text")[-1] == "Enabled":
        buttonAccept.config(text = "Disabled")
    else:
        buttonAccept.config(text = "Enabled")
        root.after(2000, accept)

def toggleSelectButton():
    if buttonSelect.config("text")[-1] == "Enabled":
        buttonSelect.config(text = "Disabled")
    else:
        buttonSelect.config(text = "Enabled")
        root.after(2000, select)

def toggleBanButton():
    if buttonBan.config("text")[-1] == "Enabled":
        buttonBan.config(text = "Disabled")
    else:
        buttonBan.config(text = "Enabled")
        root.after(2000, ban)

# UI
root= tk.Tk()
root.title("Auto Acceptor")
canvas = tk.Canvas(root, width = 400, height = 400)
labelAccept = tk.Label(root, text = "Auto accept match")
buttonAccept = tk.Button(pady = 5, padx = 30, text = "Disabled", bg = "black", fg = "white", command = toggleAcceptButton)

labelSelect = tk.Label(root, text = "Auto select champion")
global entrySelect
entrySelect = tk.Entry(root, width = 40)
entrySelect.focus_set()
buttonSelect = tk.Button(pady = 5, padx = 30, text = "Disabled", bg = "black", fg = "white", command = toggleSelectButton)

labelBan = tk.Label(root, text = "Auto ban champion")
global entryBan
entryBan = tk.Entry(root, width = 40)
entryBan.focus_set()
buttonBan = tk.Button(pady = 5, padx = 30, text = "Disabled", bg = "black", fg = "white", command = toggleBanButton)

canvas.pack()
canvas.create_window(200, 25, window = labelAccept)
canvas.create_window(200,75, window = buttonAccept)

canvas.create_window(200, 150, window = labelSelect)
canvas.create_window(200, 175, window = entrySelect)
canvas.create_window(200, 225, window = buttonSelect)

canvas.create_window(200, 300, window = labelBan)
canvas.create_window(200, 325, window = entryBan)
canvas.create_window(200, 375, window = buttonBan)

root.mainloop()