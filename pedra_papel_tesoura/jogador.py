from action import Action


class Jogador:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.escolha: Action

    def joga(self, escolha: Action):
        self.escolha = escolha
