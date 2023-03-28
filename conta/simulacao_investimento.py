from account import Account
from interface import Interface

class SimulacaoInvestimento:
    def __init__(self,conta: Account, aporte_mensal: float, numero_anos: int, porcentual_juros: float) -> None:
        self.conta = conta
        self.porcento = porcentual_juros/100
        self.aporte = aporte_mensal
        self.tempo_anos = numero_anos

        self.total_investido = 0
        self.interface = Interface(conta)

    def fazer_simulacao(self):
        for ano in range(1, (self.tempo_anos + 1)):
            self.interface.print_titulo_ano(ano)
            for mes in range(1, 13):
                self.passar_mes()
                self.interface.print_resultado_mes(mes)

        self.interface.print_resultado_total(self.total_investido)

    def calcular_juros_mensal(self) -> float:
        return (self.conta.saldo * self.porcento)

    def render_saldo(self):
        self.conta.depositar(self.calcular_juros_mensal())

    def fazer_aporte(self):
        self.conta.depositar(self.aporte)
        self.total_investido += self.aporte
        
    def passar_mes(self,):
        self.fazer_aporte()
        self.render_saldo()