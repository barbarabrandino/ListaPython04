print("Nome: Bárbara Helena Preto Brandino \n RA: \n Curso: DSM")
print()
import math
valor=int(input("Digite um valor:"))
if valor in [1,2]:
    resultado=valor**2
    print("O valor em **2 é", resultado)
elif valor % 3==0:
    resultado= math.factorial(valor)
    print("Resultado do fatorial é",resultado)
elif valor in [4,5,7,8]:
    resultado= valor/9
    print("Resultado dividio por 9 é",resultado)
else:
    print("Valor inválido")
    #Comentário geral do código: Usei a biblioteca math para pode realizar o calculo do fatorial, além disso foi emcionado math.fatorial!
    #Valor foi considerado inteiro e habilitado
    