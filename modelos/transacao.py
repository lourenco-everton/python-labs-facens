from utils.utils import Utils

class Transacao():
    def __init__(self, tipo = None, valor = None, descricao = None):
        self.__utils = Utils()

        self.__tipo = tipo
        self.__valor = valor
        self.__descricao = descricao

    def salvar(self):
        self.__utils.escrever_arquivo(
            self.__tipo, self.__valor, self.__descricao
        )

    def visualizar(self):
        for t in self.__utils.ler_arquivo():
            print(f"{t} \r\n")