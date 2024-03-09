import pyautogui
import pyscreeze
import time


def reel():
    while
    reel = pyautogui.locateOnScreen('reel_right_side.png', grayscale=True, confidence=.9)
    pyautogui.moveTo(reel)
    pyautogui.click()


def main():
    print('test')

    duel = pyautogui.locateOnScreen('cast.png', grayscale=True, confidence=.9)

    pyautogui.moveTo(duel)
    pyautogui.click()
    print(duel)

    time.sleep(1)

    duel = pyautogui.locateOnScreen('release.png', grayscale=True, confidence=.9)

    pyautogui.moveTo(duel)
    pyautogui.click()



main()
