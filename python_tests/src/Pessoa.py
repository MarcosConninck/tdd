import requests


class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.dados_obtidos = False

    def obter_todos_os_dados(self):
        response = requests.get('')

        if response.ok:
            self.dados_obtidos = True
            return 'CONECTADO'
        else:
            self.dados_obtidos = False
            return 'ERRO 404'
