import pyautogui

pegar=str(input("posicione seu mouse e digite p para marcar local das pokeballs: "))
if pegar == "p":
    pb = pyautogui.position()

while True:

    cramperl = pyautogui.locateOnScreen('clamperl.PNG', confidence=0.7)

    if cramperl != None:

        pyautogui.locateOnScreen('clamperl.PNG', confidence=0.7)
        print('achei')

        x_cramperl, y_cramperl = pyautogui.center(cramperl)
    
        pyautogui.moveTo(pb)
        pyautogui.rightClick()

        pyautogui.moveTo(x_cramperl, y_cramperl)
        pyautogui.click()

