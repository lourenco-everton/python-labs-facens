
from config.configuracoes import Configuracoes
from datetime import date

class Utils():
    def __init__(self):
        self.__conf = Configuracoes()

    def ler_arquivo(self):
        with open(self.__conf.arquivo_saida, "r") as arquivo:
            # Toda vez que lemos o read, ele retorna \n
            return list( map ( lambda l: l.replace("\n", ""), arquivo.readlines() ) )

    def escrever_arquivo(self, tipo, valor, descricao):
        with open(self.__conf.arquivo_saida, "a+") as arquivo:
            arquivo.write(f"{str(date.today())} - {tipo} - R$ {valor} - {descricao}")