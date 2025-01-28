import os
import escolher_opcao
import exibir_opcoes
import exibir_nome_do_programa

# sequencia das funcoes que seram chamadas
def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()