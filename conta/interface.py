from account import Account


class Interface:
    def __init__(self, conta: Account) -> None:
        self.conta = conta
    
    def print_titulo_ano(self, ano: int):
        print(f"\n---------- {ano}° ano ----------\n")
    
    def print_resultado_mes(self, mes: int):
        print(f"mês {mes} - saldo de {self.conta.saldo:,.2f}")
    
    def print_resultado_total(self, total_investido: float):
        print(f"""
Olá {self.conta.nome},
ao longo dos meses você investiu um total de R${total_investido:,.2f} reais, 
e no fim você garantiu R${self.conta.saldo:,.2f} reais, um lucro de R${(self.conta.saldo - total_investido):,.2f}""")