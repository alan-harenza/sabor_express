import alternar_estado_do_restaurante
import cadastrar_novo_restaurante
import listar_restaurantes
from utils.opcao_invalida import opcao_invalida
from utils.finalizar_app import finalizar_app


def escolher_opcao():
    '''
    Solicita e executa a opção escolhida pelo usuário

    Inputs:
    - um número de acordo com o menu a ser selecionado

    Outputs:
    - Executa a opção escohlida pelo usuário
    '''
    # nome de variaveis em python deve se usar underscore_case
    # ou seja, tudo minusculo e separado por underscore (ou underline)
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()
        
        elif opcao_escolhida == 4:
            finalizar_app()

        else:
            opcao_invalida()

    except:
        opcao_invalida()