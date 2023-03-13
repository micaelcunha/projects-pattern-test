from action import Action
from jogador import Jogador


class Partida:
    def __init__(self, jogador_1: Jogador, jogador_2: Jogador) -> None:
        self.jogador_1 = jogador_1
        self.jogador_2 = jogador_2
        self._vencedor: Jogador

    @property
    def vencedor(self):
        return self._vencedor

    @vencedor.setter
    def vencedor(self, jogador: Jogador):
        if self._vencedor == jogador:
            return
        self._vencedor = jogador

    def definir_reultado(self) -> None:
        if(self.empate()):
            self.definir_empate()
            return
        self.definir_vencedor(self.quem_venceu())

    def empate(self) -> bool:
        if (self.jogador_1.escolha == self.jogador_2.escolha):
            return True
        
    def definir_empate(self) -> None:
        empate = Jogador("Empate")
        self._vencedor = empate

    def quem_venceu(self) -> Jogador:
        jogadas = [self.jogador_1.escolha, self.jogador_2.escolha]
        match jogadas:
            case [Action.PEDRA, Action.TESOURA]:
                return self.jogador_1
            case [Action.PEDRA, Action.PAPEL]:
                return self.jogador_2
            case [Action.TESOURA, Action.PEDRA]:
                return self.jogador_2
            case [Action.TESOURA, Action.PAPEL]:
                return self.jogador_1
            case [Action.PAPEL, Action.PEDRA]:
                return self.jogador_1
            case [Action.PAPEL, Action.TESOURA]:
                return self.jogador_2
            case _:
                pass
    
    def definir_vencedor(self, vencedor: Jogador) -> None:
        self._vencedor = vencedor