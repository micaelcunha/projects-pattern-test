from interface import Interface
from jogador import Jogador
from partida import Partida
from action import Action



def chamar_resultado(partida: Partida, interface: Interface) -> None:
    partida.definir_reultado()
    if(partida.empate()):
        interface.escrever_empate()
        return
    interface.escrever_nome_vencedor(partida.vencedor.nome)

def pegar_input(interface) -> str:
    return interface.input()
    

def input_valido(escolha: str) -> bool:
    try:
        escolha = int(escolha.replace(""))
    except:
        return False
    if((escolha == 1) or (escolha == 2) or (escolha == 3)):
        return True
    return False

def jogada(escolha: int) -> Action:
    match escolha:
        case 1:
            return Action.PEDRA
        case 2:
            return Action.PAPEL
        case 3:
            return Action.TESOURA

def chamar_jogada(jogador: Jogador, interface: Interface) -> None:
    interface.escrever_jogadas_possiveis(jogador.nome)
    input = pegar_input(interface)
    while (input_valido(input)):
        jogador.joga(jogada(input))
    else:
        print("error")



interface = Interface()

jogador_1 = Jogador(interface.chamar_jogador_1())
jogador_2 = Jogador(interface.chamar_jogador_2())

partida = Partida(jogador_1, jogador_2)

chamar_jogada(jogador_1, interface)
chamar_jogada(jogador_2, interface)
    
chamar_resultado(partida, interface)