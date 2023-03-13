class Interface:
    def __init__(self) -> None:
        print("Seja bem vindo ao Pedra Papel Tesoura")

    def chamar_jogador_1(self) -> str:
        nome_jogador_1 = input("Digite o nome do jogador-1. ")
        return nome_jogador_1

    def chamar_jogador_2(self) -> str:
        nome_jogador_2 = input("Digite o nome do jogador-2. ")
        return nome_jogador_2
    
    def escrever_jogadas_possiveis(self, nome_jogador:str) -> None:
        print(f"""{nome_jogador} aperte o numero correspondente a sua jogada desejada
    1 - Pedra
    2 - Papel
    3 - Tesoura
        """)
    
    def input(self) -> str:
        return input()
    
    def escrever_nome_vencedor(self, nome_jogador: str) -> None:
        print(f"Parabéns {nome_jogador}!! Você venceu a partida.")

    def escrever_empate(self) -> None:
        print("Jogadas iguais!! Deu empate.")