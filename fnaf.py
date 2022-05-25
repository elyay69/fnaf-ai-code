import pyautogui
import time
from checkchica import *

rt = True
wind = False
hr = False

def winding():
    pyautogui.moveTo(748, 758)
    pyautogui.moveTo(1184, 490)
    pyautogui.click() 
    px = pyautogui.pixel(946,448)
    print(px)
    if px[0] == 0:
        pyautogui.moveTo(448, 748)
        pyautogui.moveTo(948, 658, 0.1)
        time.sleep(2)
        pyautogui.keyUp("ctrl")
        time.sleep(6)
        pyautogui.moveTo(448, 748)
        pyautogui.moveTo(948, 658, 0.1)
        flashfox()
        winding()
    else:
        pyautogui.moveTo(546, 626)
        pyautogui.mouseDown()
        px = pyautogui.pixel(946,448)
        print(px)
        if px[0] == 0:
            pyautogui.mouseUp()
            pyautogui.moveTo(448, 748)
            pyautogui.moveTo(948, 658, 0.1)
            time.sleep(2)
            pyautogui.keyUp("ctrl")
            time.sleep(6)
            pyautogui.moveTo(448, 748)
            pyautogui.moveTo(448, 658, 0.1)
            pyautogui.moveTo(1072, 447, 0.7)
            flashfox()
            winding()
        else:
            px = pyautogui.pixel(946,448)
            print(px)
            if px[0] == 0:
                pyautogui.mouseUp()
                pyautogui.moveTo(448, 748)
                pyautogui.moveTo(448, 658, 0.1)
                time.sleep(2)
                pyautogui.keyUp("ctrl")
                time.sleep(6)
                pyautogui.moveTo(448, 748)
                pyautogui.moveTo(448, 658, 0.1)
                pyautogui.moveTo(1072, 447, 0.7)
                flashfox()
                winding()
            else:
                px = pyautogui.pixel(946,448)
                print(px)
                if px[0] == 0:
                    pyautogui.mouseUp()
                    pyautogui.moveTo(448, 748)
                    pyautogui.moveTo(448, 658, 0.1)
                    time.sleep(2)
                    pyautogui.keyUp("ctrl")
                    time.sleep(6)
                    pyautogui.moveTo(448, 748)
                    pyautogui.moveTo(448, 658, 0.1)
                    pyautogui.moveTo(1072, 447, 0.7)
                    flashfox()
                    winding()
                else:      
                    px = pyautogui.pixel(946,448)
                    print(px)
                    if px[0] == 0:
                        pyautogui.mouseUp()
                        pyautogui.moveTo(448, 748)
                        pyautogui.moveTo(448, 658, 0.1)
                        time.sleep(2)
                        pyautogui.keyUp("ctrl")
                        time.sleep(6)
                        pyautogui.moveTo(448, 748)
                        pyautogui.moveTo(448, 658, 0.1)
                        pyautogui.moveTo(1072, 447, 0.7)
                        flashfox()
                        winding()
                    else:
                        px = pyautogui.pixel(946,448)
                        print(px)
                        if px[0] == 0:
                            pyautogui.mouseUp()
                            pyautogui.moveTo(448, 748)
                            pyautogui.moveTo(448, 658, 0.1)
                            time.sleep(2)
                            pyautogui.keyUp("ctrl")
                            time.sleep(6)
                            pyautogui.moveTo(448, 748)
                            pyautogui.moveTo(448, 658, 0.1)
                            pyautogui.moveTo(1072, 447, 0.7)
                            flashfox()
                            winding()
                        else:
                            pyautogui.mouseUp()
                            pyautogui.moveTo(748, 758)
                            pyautogui.moveTo(748, 658)
                            pyautogui.moveTo(448, 758)
                            pyautogui.moveTo(748, 658)
                            time.sleep(0.5)
                            pyautogui.moveTo(448, 758)   
                            pyautogui.moveTo(748, 658)  
                            mask = pyautogui.pixel(20,788) 
                            print(mask)
                            if mask[0]==0:
                                time.sleep(7)
                                pyautogui.moveTo(448, 758) 
                                pyautogui.moveTo(748, 658)
                                pyautogui.moveTo(1072, 447, 0.7)
                                flashfox()
                                winding() 




def routine(hide):
    pyautogui.moveTo(0, 447)
    time.sleep(0.6)
    pyautogui.moveTo(199, 446)
    pyautogui.mouseDown()
    left = pyautogui.pixel(135, 671)
    pyautogui.mouseUp()
    print (left)
    if left[0] != 25:
        pyautogui.keyDown("ctrl")
        hr = True
        hide = True
    else:
        pyautogui.keyDown("ctrl")
        pyautogui.moveTo(1072, 447)
        time.sleep(0.5)
        pyautogui.keyUp("ctrl")
        pyautogui.mouseDown()
        right = pyautogui.pixel(1103,646)
        pyautogui.mouseUp()
        print(right)
        if right[0] != 41:
            hr = False
            hide = True 
        else:
            pyautogui.mouseUp()
    if hide == True:
        time.sleep(0.1)
        pyautogui.moveTo(448, 748)
        pyautogui.moveTo(948, 658, 0.1)
        time.sleep(1)
        pyautogui.keyUp("ctrl")
        time.sleep(6)
        pyautogui.moveTo(448, 748)
        pyautogui.moveTo(748, 658, 0.1)
        flashfox()
        winding()
    else:
        winding()

print("start")
time.sleep(30)
seconds = time.time()
while True:
    routine(False)
    second2 =time.time()
    a = second2-seconds
    if a>=408:
        print("6 seconds have passed")
        break