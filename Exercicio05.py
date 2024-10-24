print("Nome: Bárbara Helena Preto Brandino \n RA: \n Curso: DSM")
print()

# Solicita o valor da compra
compra = float(input("Digite o valor da compra: R$ "))

# Aplica os descontos conforme o valor da compra
if compra > 300:  # 20% de desconto para compras acima de 300
    valor = compra - (compra * 0.20)
elif 200 <= compra <= 299.99:  # 10% de desconto para compras entre 200 e 299.99
    valor = compra - (compra * 0.10)
else:  # 5% de desconto para compras abaixo de 200
    valor = compra - (compra * 0.05)
# Exibe o valor com o desconto aplicado
print("O valor com desconto é:", valor)
