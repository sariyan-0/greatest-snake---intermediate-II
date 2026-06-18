####################### Python Automate Graphical Interface #######################
import pyautogui

screen_size = pyautogui.size()
print(screen_size)
# -----------------------------
# pyautogui.moveTo(x=1000, y=100, duration=0.1)
# will move 1000 px in X direction and 100 in Y
# pyautogui.move(10, 0, duration=3)
#
# pyautogui.move(400, 400, duration= 3)
# -----------------------------
# pyautogui.moveTo(x=30, y=1050, duration=2)
# pyautogui.click()
# ---------------- combine moveTo and click
# pyautogui.click(x=30, y=1050, duration=2)
#
# pyautogui.click(x=30, y=1050, duration=2, button='right')
#
# pyautogui.click(x=30, y=1050, duration=2, clicks=3, interval=5)
# ---------------------------------------------------------------
pyautogui.moveTo(x=50, y=150, duration=2)
pyautogui.dragTo(x=150, y=700, duration=2)
