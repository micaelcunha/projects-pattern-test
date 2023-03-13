def input_jogadas_possiveis() -> int:
        jogada = 2
        match jogada:
            case 1:
                return 1
            case 2:
                return 2
            case 3:
                return 3


num = input_jogadas_possiveis()
print(num)