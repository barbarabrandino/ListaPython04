print("Nome: Bárbara Helena Preto Brandino \n RA: \n Curso: DSM")
print()
# Solicita o valor inicial
valor = float(input("Digite um valor: "))

# Condição 1: se o valor for negativo, mostra o módulo (valor sem sinal)
if valor < 0:
    print("O módulo do valor é:", abs(valor))

# Condição 2: se o valor for maior do que 10, solicita outro valor e mostra a diferença
elif valor > 10:
    valor2 = float(input("Digite outro valor: "))
    diferenca = valor - valor2
    print("A diferença entre os valores é:", diferenca)

# Condição 3: caso não seja nenhuma das anteriores, divide o valor por 5
else:
    resultado = valor / 5
    print("O valor dividido por 5 é:", resultado)
