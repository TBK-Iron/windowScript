from pyautogui import getWindowsWithTitle
from time import sleep

# Get the current position of the active window
window = getWindowsWithTitle("Chrome")[0]

window.restore()
sleep(0.0001)
window.moveTo(-2000,0)
sleep(0.0001)
window.maximize()