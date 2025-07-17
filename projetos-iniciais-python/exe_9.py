# Faça um programa que calcula e exibe o salário reajustado de um funcionário. O percentual de aumento;

salario = float(input("Digite seu salário: "))

if (salario < 300):
    percentual = 0.45

elif (salario >= 300 and salario <= 600):
    percentual = 0.25

else:
    percentual = 0.15

aumento = salario * percentual
novo_salario = salario + aumento
print("Seu novo salário é de R$",novo_salario)
