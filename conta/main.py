from conta_juros import ContaService
from conta_nu import Account


def passar_mes(conta: Account, juros: ContaService):
    conta.depositar(100)
    juros.render_saldo(conta)

def passar_ano(conta: Account, juros: ContaService):
    for mes in range(12):
        passar_mes(conta, juros)

contaNu = Account("Micael")
juros = ContaService(2.73)

passar_mes(contaNu, juros)
passar_mes(contaNu, juros)

print(contaNu.saldo)