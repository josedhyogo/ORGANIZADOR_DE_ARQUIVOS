import os
import shutil
from time import sleep
import PySimpleGUI as sg


def criar_pastas(values):
    """Cria as pastas escolhidas pelo usuário e retorna seus destinos."""

    # Relaciona cada chave da interface às suas respectivas extensões
    chaves = {
        "-JPG-": [".jpg", ".jpeg"],
        "-PDF-": [".pdf"],
        "-EXE-": [".exe"]
    }

    # Armazena a relação entre a extensão e sua pasta de destino
    destinos = {}

    for chave, extensoes in chaves.items():

        pasta = values[chave]  # Obtém o valor associado à chave

        if pasta:

            # Cria a pasta caso ela não exista
            os.makedirs(pasta, exist_ok=True)

            # Relaciona cada extensão ao destino escolhido
            for extensao in extensoes:
                destinos[extensao] = pasta

    return destinos


def abrir_diretorio_principal():
    """Solicita ao usuário o diretório que será organizado."""

    # Abre uma janela para o usuário selecionar a pasta
    receber_caminho = sg.popup_get_folder("Digite o caminho da pasta:")

    caminho = os.path.expanduser(receber_caminho)
    os.chdir(caminho)

    # Obtém os arquivos e pastas presentes no diretório
    arquivos = os.listdir()

    return arquivos


# IDEIA -> SEPARAR A FUNÇÃO MOVER ARQUIVOS E A CRIAR PASTAS PARA ORGANIZAR SEM CRIAR OU ORGANIZA CRIANDO PASTAS

def mover_arquivos(arquivos, values):
    """Move os arquivos para as pastas escolhidas pelo usuário."""

    # Cria as pastas e obtém seus respectivos destinos
    destinos = criar_pastas(values)
    pasta_outros = values["-OUTROS-"]

    # Obtém a quantidade total de itens para a barra de progresso
    num_arquivos = len(arquivos)

    # Percorre todos os itens encontrados no diretório
    for i, arquivo in enumerate(arquivos):

        # Atualiza a barra de progresso
        sg.one_line_progress_meter("MOVENDO ARQUIVOS",i + 1,num_arquivos)

        sleep(0.1)

        # Ignora diretórios, processando apenas arquivos
        if os.path.isdir(arquivo):
            continue

        # Obtém a extensão do arquivo
        extensao = os.path.splitext(arquivo.lower())[1]

        # Move o arquivo para o destino correspondente
        if extensao in destinos:
            shutil.move(arquivo, destinos[extensao])

        # Caso a extensão não esteja configurada, envia para "outros"
        else:
            os.makedirs(pasta_outros, exist_ok=True)
            shutil.move(arquivo, "outros/")


    sg.popup_ok("OPERAÇÃO CONCLUÍDA COM SUCESSO!")


# Interface gráfica
layout = [
    [sg.Text("ORGANIZADOR DE ARQUIVOS")],
    [sg.Text("JPG/JPEG: "), sg.Input(key="-JPG-")],
    [sg.Text("PDF: "), sg.Input(key="-PDF-")],
    [sg.Text("EXE: "), sg.Input(key="-EXE-")],
    [sg.Text("OUTROS: "), sg.Input(key="-OUTROS-")],
    [sg.Button("ORGANIZAR")]
]


# Cria a janela principal
window = sg.Window("Organizador de Arquivos", layout)


# Loop principal da interface
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "ORGANIZAR":
        arquivos = abrir_diretorio_principal()
        mover_arquivos(arquivos, values)
