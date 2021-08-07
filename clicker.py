import pyautogui
from pynput.keyboard import *

#delay for clicking
delay = 1
resume_key = Key.f1 
pause_key = Key.f2
exit_key = Key.esc

#False to disable these 
pause = True
running = True

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("Resumed")
    elif key == pause_key:
        pause = True
        print("Paused")
    elif key == exit_key:
        running = False
        print("Exited")


def display_controls():
    print("Controls:")
    print("F1 = Resume")
    print("F2 = Pause")
    print("Esc = Exit")
  

def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
    lis.stop()


if __name__ == "__main__":
    main()
