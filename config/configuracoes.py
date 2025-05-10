class Configuracoes():
    def __init__(self):
        self.__arquivo_saida = "./saida/transacoes.txt"

    @property
    def arquivo_saida(self):
        return self.__arquivo_saida