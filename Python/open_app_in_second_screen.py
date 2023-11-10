import pygetwindow as gw
import subprocess
import time

def openApp(posicao_x, posicao_y, caminho, nome):
    # Execute o comando para abrir o aplicativo
    subprocess.Popen(caminho)

    # Aguarde um pequeno intervalo para garantir que o aplicativo tenha tempo para abrir
    time.sleep(1)

    # Encontre a janela do aplicativo pelo título ou parte do título
    janela = gw.getWindowsWithTitle(nome)[0]
    # ou janela = gw.getWindowsWithTitle("Parte_do_Título")[0]

    # Defina a posição da janela
    janela.moveTo(posicao_x, posicao_y)

    # Maximize a janela (opcional)
    janela.maximize()
    # Traga a janela para frente (opcional)
    janela.activate()


# Exemplo de Uso
openApp(1920, 10, r"calc", "Calculadora")
