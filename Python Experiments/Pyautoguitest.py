import pyautogui as pgui, webbrowser, time

x = 50

while x > 0 :
    print(x)
    pgui.hotkey('command', 'r')
    time.sleep(5)
    x = x - 1 