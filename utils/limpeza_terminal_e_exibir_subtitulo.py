import os

def limpeza_terminal_e_exibir_subtitulo(texto):
    '''
    Limpa o terminal e exibe um subtítulo estilizado na tela

    Inputs:
    - texto: str - O texto do subtítulo
    '''
    os.system('clear')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)