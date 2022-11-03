"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo
lógico e hierárquico utilizando classes

Encapsular -> cápsula


            classe  
------------------------------
|                            |
|    ATRIBUTOS E METODOS     |
------------------------------

# Relembrando Atributos/Metodos privados em Python

Imagine que temos uma classe chamada Pessoa, contendo um atributo privado
chamado __nome e um método privado chamado __falar()

Esses elementos privados só devem/deveriam ser acessados dentro da classe.
Mas Python não bloqueia este acesso fora da classe. Com Python acontece um
fenômeno chamado Name Mangling, que faz uma alteração na forma de se acessar
os elementos privados, conforme:

_Classe__elemento

Exemplo - acessando elementos privados fora da classe:

instancia._Pessoa__nome
instancia._Pessoa__falar()

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe,
escondendo 


# DESSA FORMA MEUS ATRIBUTOS NAO SAO PRIVADOS: 
class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador
        self.titular = titular
        self.saldo = saldo 
        self.limite = limite 
        Conta.contador += 1 

    def extrato(self):
        print(f'Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}')

    def depositar(self, valor):
        self.saldo += valor 

    def sacar(self, valor):
        self.saldo -= valor         


# testes 
conta1 = Conta('Jabon', 150, 1500)

print(f'numero da conta: {conta1.numero}')

print(f'nome do titular: {conta1.titular}')

print(f'saldo: {conta1.saldo}')


print(f'limite: {conta1.limite}')

conta1.numero = 42
conta1.titular = 'xuxa'
conta1.saldo = 99999
conta1.limite = 99999999

print(conta1.__dict__)


conta1.extrato()


"""



# DESSA FORMA MEUS ATRIBUTOS SAO PRIVADOS: 

class Conta2:
    
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta2.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta2.contador += 1

    def extrato(self):
        print(f'Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('Ta querendo me passar a perna?')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente')
        else:
            print('Valor invalido')


conta2 = Conta2('Jabon', 150, 1500)

print(conta2.__dict__)

conta2.depositar(-150)

print(conta2.__dict__)

conta2.sacar(200)

print(conta2.__dict__)
