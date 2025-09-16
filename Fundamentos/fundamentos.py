# Strings
# Função len() conta os caracteres de uma string bem como os espaços.
# nome = "Cesar Augusto de Jesus"
# print(len(nome))

# Podemos a partir de um índice indicado pela função len() capturar esse mesmo índice por meio dos colchetes [].
# print(nome[6])

# Podemos concatenar strings com o operador '+' ou repetir com o operador '*'
# print("Cesar " + "Augusto " + "de " + "Jesus")
# print("Eu te amo" + " muito" * 3 + "!")

# Podemos realizar composição entre variáveis de vários tipos para exibição de mensagens
nome = "Cesar"
idade = 40
cidade = "São Paulo - SP"
salario = 2500.0

print("Olá %s. Sua idade é %d anos e você mora em %s" % (nome,idade,cidade)) # Forma anterior ao python 3
print("Olá {}. Sua idade é {} anos e você mora em {}".format(nome,idade,cidade)) # Forma a partir do python 3
print("Nome: {} | Idade: {} | Cidade: {} | Salário: R${:5.2f}".format(nome,idade,cidade,salario)) # Máscara para valores monetários
print(f"Nome: {nome} | Idade: {idade} | Cidade: {cidade} | Salário: R${salario:5.2f}") # Forma a partir do python 3.6