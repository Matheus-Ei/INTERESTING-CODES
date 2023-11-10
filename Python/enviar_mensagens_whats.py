import pywhatkit as kit
import time
import pyautogui

def enviar_mensagem(country_code, number, message):
    print("Enviando Mensagem...")
    kit.sendwhatmsg_instantly(f"{country_code}{number}", message, wait_time=15)

    time.sleep(3)  # Atraso para dar tempo de o WhatsApp abrir e a mensagem ser digitada
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'w')
    print("<<Mensagem Enviada com Sussesso>>")
