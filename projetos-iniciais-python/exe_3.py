#Faça um programa que leia três valores inteiros A, B e C e diga se a soma de A + B é menor que C;

valor_a = int(input("Digite valor A: "))
valor_b = int(input("Digite valor B: "))
valor_c = int(input("Digite valor C: "))

valor_ab = (valor_a + valor_b)

if (valor_ab < valor_c):
    print("A soma é menor que valor c ")

else:
    print("A soma é maior do que valor c")
