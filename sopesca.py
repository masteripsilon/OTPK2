import pyautogui
import time
import keyboard
import winsound

battle=str(input("posicione seu mouse e digite b para marcar posicao do target: "))
if battle == "b":
    bt=pyautogui.position()

agua=str(input("posicione seu mouse e digite l para marcar posicao na agua: "))
if agua == "l":
    ag  = pyautogui.position() 

while True:

        peixe = pyautogui.locateOnScreen('peixe.png', confidence=0.7)

        if peixe != None:

                peixe = pyautogui.locateOnScreen('peixe.png', confidence=0.7)
                x_peixe, y_peixe = pyautogui.center(peixe)
                pyautogui.moveTo(x_peixe, y_peixe, 0.09)
                pyautogui.click()

                vara = pyautogui.locateOnScreen('vara.PNG', confidence=0.7)
                x_vara, y_vara = pyautogui.center(vara)
                pyautogui.moveTo(x_vara, y_vara)
                pyautogui.click()

                pyautogui.moveTo(ag)
                pyautogui.click()

                pyautogui.moveTo(bt)
                pyautogui.click()

                pyautogui.press("f1")
                pyautogui.press("f2")
                pyautogui.press("f3")
                pyautogui.press("f4")
                pyautogui.press("f5")
                pyautogui.press("f6")
                pyautogui.press("f7")
                pyautogui.press("f8")
                pyautogui.press("f9")
                pyautogui.press("f10")
