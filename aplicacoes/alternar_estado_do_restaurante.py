from utils.limpeza_terminal_e_exibir_subtitulo import limpeza_terminal_e_exibir_subtitulo
from utils.voltar_menu_principal import voltar_menu_principal

def alternar_estado_do_restaurante():
    '''
    Essa função é responsável por mudar o status do restaurente.

    Input:
    - Nome do restaurante

    Output:
    - Alteração do status do restaurante ou
    - mensagem de restaurante não encontrado
    '''
    limpeza_terminal_e_exibir_subtitulo('Alterando o estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in lista_restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso ' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    
    voltar_menu_principal()


lista_restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
                      {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
                      {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}
]
