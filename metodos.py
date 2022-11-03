"""
POO - Métodos 

- Métodos (funções) -> Representam os comportamentos do objeto. 
Ou seja, as ações que este objeto pode realizar no seu sistema

Em Python, dividimos os métodos em 2 grupos: Métodos de instância e Métodos de Classe.

# Métodos de Instância

# Método dunder init __init__ é um método especial chamado de construtor e sua função é construir 
o objeto a partir da classe.

# OBS: Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline)

# OBS: Os métodos/funções dunder em Python são chamados de métodos mágicos 

Atenção! -> Por mais que possamos criar próprias funções utilizando duder (underline no início e no fim) não é
aconselhado. Python possui vários métodos com esta forma de nomenclatura e pode ser que mudemos o comportamento dessas
funções mágicas internas da linguagem. Então evite ao máximo. 

# Métodos são escritos em letras minúsculas. Se o nome for composto, o nome terá as palávras separadas por 
underline (_). 

#######################################
p1 = Produto('Play4','Video Game', 3000)

print(p1.desconto(50))
print(Produto.desconto(p1, 50))

user1 = Usuario('Matheus', 'Bonjour','matheus.bonjour@gmail.com', '123456')
user2 = Usuario('Maisa', 'Minata', 'maisaminata@hotmail.com', '654321')

print(user1.nome_completo())
print(user2.nome_completo())

print(Usuario.nome_completo(user1))

#print(user1._Usuario.__nome)

print(f'Senha User1: {user1._Usuario__senha}')
print(f'Senha User2: {user1._Usuario__senha}')





"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome 
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""
        return (self.__valor * (100 - porcentagem)) / 100
    
    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False 



from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False 

    

nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o email: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
    print('Usuário criado com Sucesso!')
else:
    print('Senha não confere! ')
    exit(42)

senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso Negado')

print(f'Senha User Criptografada: {user._Usuario__senha}')


