"""
POO - Objetos   

Objetos -> são instancias de classe.
Ou seja, após o mapeamento do objeto do mundo real para
sua representação computacional, devemos poder criar quantos objetos forem necessários. Podemos
pensar nos objetos/ instancias de uma classe como variaveis do tipo definido na classe.




#Instancias/Objetos
Lamp1 = Lampada('verde',127,60)

CC1 = ContaCorrente(5000,20000)

user1 = Usuario('Matheus','Bonjour','matheus.bonjour@gmail.com','123456')

Lamp1.ligar_desligar()
print(f'A lampada esta ligada? {Lamp1.checa_lampada()}')
"""

class Lampada:  
    
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False
    
    def checa_lampada(self):
        return self.__ligada
    
    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf 

    def diz(self):
        print(f'O cliente {self.__nome} diz oi')




class ContaCorrente:

    contador = 4999

    def __init__(self,limite,saldo, cliente):
        self.__numero = ContaCorrente.contador +1
        self.__limite = limite
        self.__saldo = saldo 
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é: {self.__cliente._Cliente__nome}')

class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome 
        self.__email = email
        self.__senha = senha


# lamp = Lampada() -> nao irá funcionar pois precisa de argumentos

nome = 'Matheus'
sobrenome = 'Bonjour'
email = 'mb@gmail.com'
senha = 'dog15'

user = Usuario(nome, sobrenome, email, senha)

print(user._Usuario__senha)

clientela = Cliente('matheus bonjour', '123.423.423-01')

cc =ContaCorrente(2000, 10000, clientela)

print(cc._ContaCorrente__cliente._Cliente__nome)

cc.mostra_cliente()

cc._ContaCorrente__cliente.diz()

clientela.diz()