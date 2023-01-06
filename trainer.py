import pyautogui
import time
import threading
import win32api , win32con

agua=str(input("posicione seu mouse e digite l para marcar posicao na agua: "))
if agua == "l":
    ag  = pyautogui.position()

def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def pescar():
    while True:
        barra = pyautogui.locateOnScreen('barra.PNG')
        if barra != None:
                vara = pyautogui.locateOnScreen('vara.PNG', confidence=0.7)
                x_vara, y_vara = pyautogui.center(vara)
                pyautogui.moveTo(x_vara, y_vara)
                click()
                pyautogui.moveTo(ag)
                click()
                time.sleep(1)


def localizarpeixe():
    while True:
        if pyautogui.locateOnScreen('peixe.png', confidence=0.7):
            peixe = pyautogui.locateOnScreen('peixe.png', confidence=0.7)
            x_peixe, y_peixe = pyautogui.center(peixe)
            pyautogui.moveTo(x_peixe, y_peixe)
            click()
            click()
            click()
            pyautogui.press('f4')
            pyautogui.press('f5')
            pyautogui.press('f6')


if __name__ == '__main__':

    t1 = threading.Thread(target=localizarpeixe)
    t2 = threading.Thread(target=pescar)

    t1.start()
    t2.start()

    t1.join()
    t2.join()




            
            