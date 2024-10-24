print("Nome: Bárbara Helena Preto Brandino \n RA: \n Curso: DSM")
print()
nome=input("Digite seu nome:")
ra= input("Digite seu RA:")
nota1=float(input("Digite sua nota 1:"))
nota2=float(input("Digite sua nota 2:"))
media= (nota1+nota2)/2
if media >=7:
    print("Parabéns!Você passou!! Sua média foi:",media)
else:
    print(" Você ainda tem uma chance! Estude mais para o exame, sua média foi:", media)
#Comentário geral do código: Utilizei váriaveis float e habilitei o teclado para que o usuário digitasse o nome, RA e notas.
#Usei If e else para que o programa conseguisse distinguir a nota menor que 7 e mostrar a mensagem de tentar novamente no próximo exame.