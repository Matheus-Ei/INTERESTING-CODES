from pywinauto import Application
from pywinauto.timings import TimeoutError
import time as time
import pygetwindow as gw
import pyautogui
from pywinauto import Desktop
from screeninfo import get_monitors

def abrir_app_segunda_tela(app_path, app_name):
    # Abrir o aplicativo
    app = Application().start(app_path)
    time.sleep(2)
    # Encontre o aplicativo pelo título da janela
    aplicativo = gw.getWindowsWithTitle(app_name)[0]
    # Obtenha as informações sobre as telas disponíveis
    telas = get_monitors()

    time.sleep(2)

    # Mova a janela para a segunda tela
    aplicativo.move(telas[0].x, telas[0].y)

    # Maximize a janela (opcional)
    aplicativo.maximize()

    # Traga a janela para frente (opcional)
    aplicativo.activate()



# Exemplo de uso
app_path = r"calc"
app_name = "Calculadora"
abrir_app_segunda_tela(app_path, app_name)
