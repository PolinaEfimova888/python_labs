from mss import mss
import pyautogui
import time
import cv2
import numpy as np

def monitor_part(img): 
    x_dino = 493
    y_dino = 708
    box_width = 640      
    box_height = 45
    # x_dino = 606
    # y_dino = 709 
    # 590 480     620 - 11  
    cactus = img[y_dino:y_dino+box_height, x_dino:x_dino + box_width]
    
    return cactus
         
sreen_tool = mss()   
x, y = pyautogui.position()
# print(x,y)

replayBtn=(948,695)   

pyautogui.click(replayBtn)
pyautogui.keyDown('space')

count=0
while x<3270:
    img = cv2.imread(sreen_tool.shot())
    cactus = monitor_part(img)
    
    cactus_gray = cv2.cvtColor(cactus, cv2.COLOR_BGR2HSV)
    
    ready_cactus = cv2.inRange(cactus_gray, np.array([0, 0, 0]), np.array([255, 255, 100]))
         
    conts, hier = cv2.findContours(ready_cactus, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(conts)>0:
        pyautogui.keyDown('space')
        time.sleep(0.05)
        pyautogui.keyUp('space')
        count+=1
        print("jump ", count)
             
    x, y = pyautogui.position()      
