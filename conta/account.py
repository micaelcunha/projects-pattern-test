class Account:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.saldo = 0

    def depositar(self, valor: float) -> None:
        self.saldo += valor

    def sacar(self, valor:float) -> bool:
        if(valor <= self.saldo):
            self.saldo -= valor
            return True
      
        return False