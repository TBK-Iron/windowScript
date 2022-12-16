import pyautogui


# Get the current position of the active window
window = pyautogui.getWindowsWithTitle("orion")[0]

window.moveTo(0,0)
window.maximize()