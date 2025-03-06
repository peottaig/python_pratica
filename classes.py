from programa import Programa

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

class Serie(Programa):
    def __init__(self, nome, ano,  temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

atlanta = Serie('atlanta', 2018, 2)
vingadores = Filme('vingadores', 2018, 160)
vingadores.dar_likes
vingadores.dar_likes
vingadores.dar_likes
print(vingadores.nome, vingadores.ano, vingadores.likes)