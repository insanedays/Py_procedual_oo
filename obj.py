# AS CLASSES PRECISAM DE COESÃO, aplique o principio de responsabilidade única SOLID

class Conta:

#construtor __init__ inicializade atributos
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite  # o __ privatiza os atributos, encapsulamento

#metodos

    def extrato(self):
        print("{}, o valor do seu extrato é de: {}".format(self.__titular, self.__saldo))


    def deposita(self, valor):
        self.__saldo = self.__saldo + valor
        print("Foi depositado {}".format(valor))

# metodo para melhorar visualização do motivo da condição,porém será privado para evitar ser ultilizado
    def __nao_pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar > valor_disponivel or valor_disponivel < 0

    def saque(self, valor):
        if self.__nao_pode_sacar(valor):
            print("O valor do saque é maior que o do saldo, favor digiar outro valor")
        else:
            self.__saldo -= valor
            print("Operação realizade com sucesso. Foi depositado {}".format(valor))

    def transfere(self, valor, destino):
        self.saque(valor)
        destino.deposita(valor)

#GET E SET

    def get_saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular.title()

    @property   #get
    def limite(self):
        return self.__limite

    @limite.setter   #set
    def limite(self, limite):
        self.__limite = limite

#metodos estáticos, não precisam de objeto (use com cautela, pois ele remetem muito a ling. procedural
#ele não manipula as informações
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigo_bancos():
        bancos = {"BB": '001', "Caixa": "104", "Bradesco":'237'}
        return bancos

