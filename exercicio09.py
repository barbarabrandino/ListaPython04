print("Nome: Bárbara Helena Preto Brandino \n RA: \n Curso: DSM")
print()
#Habilitar o teclado do usário escrever nome e idade
nome=input("Digite seu nome aqui:")
idade=int(input("Digite sua idade aqui:"))
if idade < 18:
    print("Bem-vindo,", nome, "Você é menor de idade.")
elif idade <= 65:
    print("Bem-vindo,", nome, "Você é maior de idade e tem até 65 anos.")
else:
    print("Bem-vindo,", nome, "Você tem mais de 65 anos.")
#Condições dadas ao código com if, elif e else.