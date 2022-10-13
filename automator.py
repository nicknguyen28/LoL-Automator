import sys
import pyautogui
import tkinter as tk

def accept():
    if buttonAccept.config('text')[-1] == "Enabled":
        print("Searching!")
        acceptXY = pyautogui.locateCenterOnScreen("accept.png", confidence = 0.5)
        if acceptXY != None:
            buttonAccept.config(text="Disabled")
            pyautogui.moveTo(acceptXY, duration = 0.5)
            pyautogui.click()
        root.after(3000, accept)

def select():
    if buttonSelect.config('text')[-1] == "Enabled":
        print("Searching!")
        acceptXY = pyautogui.locateCenterOnScreen("accept.png", confidence = 0.5)
        if acceptXY != None:
            buttonSelect.config(text="Disabled")
            pyautogui.moveTo(acceptXY, duration = 0.5)
        root.after(3000, accept)

def ban():
    if buttonBan.config('text')[-1] == "Enabled":
        print("Searching!")
        acceptXY = pyautogui.locateCenterOnScreen("accept.png", confidence = 0.5)
        if acceptXY != None:
            buttonBan.config(text="Disabled")
            pyautogui.moveTo(acceptXY, duration = 0.5)
        root.after(3000, accept)

def toggleAcceptButton():
    if buttonAccept.config('text')[-1] == "Enabled":
        buttonAccept.config(text="Disabled")
    else:
        buttonAccept.config(text="Enabled")
        root.after(3000, accept)

def toggleSelectButton():
    if buttonSelect.config('text')[-1] == "Enabled":
        buttonSelect.config(text="Disabled")
    else:
        buttonSelect.config(text="Enabled")
        root.after(3000, select)

def toggleBanButton():
    if buttonBan.config('text')[-1] == "Enabled":
        buttonBan.config(text="Disabled")
    else:
        buttonBan.config(text="Enabled")
        root.after(3000, ban)

def getText():
   global entry
   global string
   string = entry.get()
   

root= tk.Tk()
root.title("Auto Acceptor")
canvas = tk.Canvas(root, width = 400, height = 400)
labelAccept = tk.Label(root, text="Auto accept match")
buttonAccept = tk.Button(pady = 5, padx = 30, text = "Disabled", bg = "black", fg = "white", command = toggleAcceptButton)

labelSelect = tk.Label(root, text="Auto select champion")
entrySelect = tk.Entry(root, width= 40)
entrySelect.focus_set()
buttonSelect = tk.Button(pady = 5, padx = 30, text = "Disabled", bg = "black", fg = "white", command = toggleSelectButton)

labelBan = tk.Label(root, text="Auto ban champion")
entryBan = tk.Entry(root, width= 40)
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