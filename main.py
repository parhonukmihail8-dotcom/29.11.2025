import pyautogui, keyboard, mouse, os
import cv2
import numpy as np

if os.path.isfile(os.path.abspath(os.path.basename("loltxt"))):
    with open("lol.txt", "r") as file:
        position = file.read()
else:
    with open("lol.txt", "w") as file:
        position = [0]

SCREEN_SIZE = pyautogui.size()
FPS = 20

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, FPS, SCREEN_SIZE)

while True:
    img = pyautogui.screenshot()
    frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    out.write(frame)

    for positi in position:
        if positi == mouse.get_position:
            pass
        else:
            position.append(mouse.get_position)

    if keyboard.is_pressed("p"):
        break

out.release()
cv2.destroyAllWindows()
with open("lol.txt", "a") as file:
    file.write(str(position))