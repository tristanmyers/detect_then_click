# TODO:
# add a pause that saves the clicks



import pyautogui
import time

r = None
i = 0
bonus_button = pyautogui.locateCenterOnScreen('bonus_button.PNG', grayscale=False)
times_clicked = 0


def clickBonusButton():
    global bonus_button
    global r
    global times_clicked
    r = bonus_button
    if r is not None:
        pyautogui.click(bonus_button)
        print('clicked button at point' + str(r))
        bonus_button = pyautogui.locateCenterOnScreen('bonus_button.PNG')
        times_clicked = times_clicked + 1
        print('times clicked: ' + str(times_clicked))
    else:
        print(r)
        bonus_button = pyautogui.locateCenterOnScreen('bonus_button.PNG')


while i == 0:
    print('checking...')
    clickBonusButton()
    print('times clicked: ' + str(times_clicked))
    time.sleep(3)
