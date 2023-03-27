from conta_nu import Account

class ContaService:
    def __init__(self, juros: float) -> None:
        self.juros = juros/100

    def render_saldo(self, conta: Account):
        conta.depositar(conta.saldo * self.juros)