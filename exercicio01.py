print("Nome: Bárbara Helena Preto Brandino \n RA: \n Curso: DSM")
# Recebe um valor do usuário
valor = float(input("Digite um valor: "))

# Verifica o valor e executa a ação correspondente
if valor in [1, 2, 3]:
    resultado = valor ** 2
    print(f"O valor {valor} elevado ao quadrado é: {resultado}")

elif valor in [4, 9]:
    resultado = math.sqrt(valor)
    print(f"A raiz quadrada de {valor} é: {resultado}")

elif valor in [6, 7, 8]:
    resultado = valor / 9
    print(f"O valor {valor} dividido por 9 é: {resultado}")

else:
    print("O valor digitado não corresponde a nenhuma das opções.")
