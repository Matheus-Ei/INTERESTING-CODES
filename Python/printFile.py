import win32print

def imprimir_arquivo(arquivo):
    # Defina a impressora padrão (você pode modificar para o nome da sua impressora)
    impressora_padrao = win32print.GetDefaultPrinter()

    # Abra o arquivo para impressão
    try:
        file_handle = open(arquivo, 'rb')
    except IOError:
        raise Exception(f"Não foi possível abrir o arquivo: {arquivo}")

    # Inicialize a impressão
    print_handle = win32print.OpenPrinter(impressora_padrao)
    job_info = win32print.StartDocPrinter(print_handle, 1, ('Imprimir arquivo', None, "RAW"))
    win32print.StartPagePrinter(print_handle)

    # Leia e imprima o conteúdo do arquivo
    while True:
        data = file_handle.read(4096)
        if not data:
            break
        win32print.WritePrinter(print_handle, data)

    # Finalize a impressão
    win32print.EndPagePrinter(print_handle)
    win32print.EndDocPrinter(print_handle)
    win32print.ClosePrinter(print_handle)

    # Feche o arquivo
    file_handle.close()

# Chamada da função para imprimir um arquivo
imprimir_arquivo(r'C:\Users\matheus.eickhoff\Downloads\Nova pasta\past\MANUAL DE COMO ABRIR E EXTRAIR  OS DOCUMENTOS ZIP.pdf')
