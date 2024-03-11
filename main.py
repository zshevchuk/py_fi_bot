import pyautogui
import pyscreeze
import time


CONFIDENCE = .9
GRAYSCALE = True

def reel():
    while True:
        reel = pyautogui.locateOnScreen('reel_right_side.png', grayscale=GRAYSCALE, confidence=CONFIDENCE)
        pyautogui.moveTo(reel)
        pyautogui.click()


def isReeling():
    return find_image("smaller_r.png")

def find_image(image_path):
    try:
        # Locate the image on the screen
        image_location = pyautogui.locateOnScreen(image_path, grayscale=GRAYSCALE, confidence=CONFIDENCE)
        return image_location

    except pyautogui.ImageNotFoundException:
        return False

def find_image_actively(image_path):
    while True:
        try:
            # Locate the image on the screen
            image_location = pyautogui.locateOnScreen(image_path, grayscale=GRAYSCALE, confidence=CONFIDENCE)

            # Check if the image is found
            if image_location is not None:
                # Perform your actions here
                print("Image found! Coordinates:", image_location)
                # Add your code to perform actions based on the image presence

            # Wait for a short time before checking again
            time.sleep(1)
        except KeyboardInterrupt:
            # Handle if the user interrupts the script (e.g., press Ctrl+C)
            print("Script interrupted by user.")
            break

        except pyautogui.ImageNotFoundException:
            # Handle if the user interrupts the script (e.g., press Ctrl+C)
            print("Not found")
            break

def main():
    print('test')

    duel = pyautogui.locateOnScreen('cast.png', grayscale=GRAYSCALE, confidence=CONFIDENCE)

    pyautogui.moveTo(duel)
    pyautogui.click()
    print(duel)

    time.sleep(1)

    duel = pyautogui.locateOnScreen('release.png', grayscale=GRAYSCALE, confidence=CONFIDENCE)

    pyautogui.moveTo(duel)
    pyautogui.click()



# main()
# Example usage
image_path = "smaller_r.png"
print(isReeling())
