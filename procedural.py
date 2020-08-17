# informações
numero = 123
titular = "Amandha"
saldo = 55.0
limite = 1000.0

# dicionário apresenta um conjunto de dados
 # conta = {'numero': 123, "titular": "Amandha", "saldo": 55.0, "limite": 1000.0}


# printa uma informação do dicionário
# print(conta["limite"])


# Função para criar conta
def criar_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta
#função para depositar na conta
def deposita(conta,valor):
    conta["saldo"] += valor

#função para sacar na conta
def saque(conta,valor):
    conta["saldo"] -= valor

# funçao para visualizar saldo
def extrato(conta):
    print("O valor da conta é {}".format(conta["saldo"]))







