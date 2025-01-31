from utils.limpeza_terminal_e_exibir_subtitulo import limpeza_terminal_e_exibir_subtitulo
from utils.voltar_menu_principal import voltar_menu_principal


def cadastrar_novo_restaurante():
    '''
    Essa função é responsavel por cadastrar um novo restaurante
    Inputs:
    - Nome do restaurante
    - Categoria
    Output:
    - Adiciona um novo restaurante a lista de restaurantes
    '''
    limpeza_terminal_e_exibir_subtitulo('cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    lista_restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_menu_principal()

lista_restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
                      {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
                      {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}
]