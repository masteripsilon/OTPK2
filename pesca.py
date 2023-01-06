import pyautogui
import time
import threading
import win32api , win32con
from discord_webhook import DiscordWebhook
import winsound

battle=str(input("posicione seu mouse e digite b para marcar posicao do target: "))
if battle == "b":
    bt=pyautogui.position()

agua=str(input("posicione seu mouse e digite l para marcar posicao na agua: "))
if agua == "l":
    ag  = pyautogui.position() 

loot=str(input("posicione seu mouse e digite u para marcar corpo: "))
if loot == "u":
    lt  = pyautogui.position()

pegar=str(input("posicione seu mouse e digite p para marcar loot: "))
if pegar == "p":
    pb  = pyautogui.position()


def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

winsound.Beep(540, 1000)

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
                

def ctrlclick():
    pyautogui.keyDown('ctrl')
    pyautogui.rightClick()
    pyautogui.keyUp('ctrl')

        

def chat():

     if pyautogui.locateOnScreen('chat.PNG'):

                pyautogui.press("tab")

                chat = pyautogui.screenshot()
                chat.save(r'C:\BOT\print.jpg')

                pyautogui.press("tab")

                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1055968269451935754/cIkPguNXCtzX1r8h5mohAzDOVYYxWHvhx_ZVtCJZzeQttlflvsxBrskm6AtPP-8twdT2', username="undermortis")

                with open(r'C:\BOT\print.jpg', 'rb') as f:
                    webhook.add_file(file=f.read(), filename='print.jpg')

                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1055968269451935754/cIkPguNXCtzX1r8h5mohAzDOVYYxWHvhx_ZVtCJZzeQttlflvsxBrskm6AtPP-8twdT2', content='@everyone')
                
              

            
def localizarpeixe():
    turn = 0
    spellsToUse = { 0: ['f1', 'f2', 'f3', 'f4', 'f8'], 1: ['f5', 'f6', 'f7', 'f9'] }
    while True:
        if pyautogui.locateOnScreen('peixe.png', confidence=0.7):
            peixe = pyautogui.locateOnScreen('peixe.png', confidence=0.7)
            x_peixe, y_peixe = pyautogui.center(peixe)
            pyautogui.moveTo(x_peixe, y_peixe)
            click()
            click()
            click()
            pyautogui.moveTo(bt)
            click()
            time.sleep(0.7)
            pyautogui.press(spellsToUse[turn])
            time.sleep(0.6)
            pyautogui.moveTo(lt)
            ctrlclick()
            time.sleep(0.3)
            pyautogui.moveTo(pb)
            click()
            click()
            click()
            pyautogui.moveTo(lt)
            time.sleep(0.1)
            pyautogui.press("f12")
            time.sleep(0.1)
            click()
            
            turn = 1 if turn == 0 else 0
            


if __name__ == '__main__':

    t1 = threading.Thread(target=localizarpeixe)
    t2 = threading.Thread(target=pescar)
    t3 = threading.Thread(target=chat)

    t1.start()
    t2.start()
    t3.start()


    t1.join()
    t2.join()
    t3.join()