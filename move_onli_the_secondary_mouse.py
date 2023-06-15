from pynput.mouse import Controller

# Crie uma instância do controlador do mouse secundário
mouse_secundario = Controller()

x = 10
y = 20

# Mova o mouse secundário para a posição (x, y)
mouse_secundario.position = (x, y)
