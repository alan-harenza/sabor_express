from utils.limpeza_terminal_e_exibir_subtitulo import limpeza_terminal_e_exibir_subtitulo
from utils.voltar_menu_principal import voltar_menu_principal

def listar_restaurantes():
    '''
    Essa função é responsável por listar os restaurantes

    Output:
    - lista dos restaurantes cadastrados
    '''
    limpeza_terminal_e_exibir_subtitulo('Listando os restaurantes')

    print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in lista_restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_menu_principal()


lista_restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
                      {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
                      {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}
]