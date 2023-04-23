# Faça um programa que receba dois números e execute as operações listadas a seguir, de acordo com a escolha do usuário;
#CÓDIGO 1; Média entre os números digitados
#CÓDIGO 2; Diferença do maior pelo menor
#CÓDIGO 3; Produto entre os números digitados
#CÓDIGO 4; Divisão do primeiro pelo segundo

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
codigo = int(input("Digite o codigo: "))

if (codigo == 1):
    media = (num1 + num2)/2
    print("A média é: ",media)

elif (codigo == 2):
    if (num1 > num2):
        resultado = num1 - num2

    else:
        resultado = num2 - num1
        print("A subtração dá: ",resultado)

elif (codigo == 3 ):
    produto = num1 * num2
    print("O resultado do produto é: ", produto)

elif (codigo == 4):
    if (num2 == 0):
        print("Divisão por zero não existe!")
    else: #num2 != 0
        resultado = num1 / num2
        print("O resultado da divisão dá: ",resultado)

else: #caso contrário
    print("Código inválido!")


