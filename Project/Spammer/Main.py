import pyautogui,time
while True:
    time.sleep(10)
    with open('main.txt', 'r') as f:
        for word in f:
            pyautogui.typewrite(word)
            pyautogui.press('enter')

