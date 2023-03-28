from account import Account
from simulacao_investimento import SimulacaoInvestimento

conta = Account("Micael")

simulacao_1 = SimulacaoInvestimento(conta, 100, 10, 2.73)
simulacao_1.fazer_simulacao()