#Faça um programa que calcula e exibe o salário reajustado de um funcionário. O percentual de aumento encontra-se na tabela a seguir;


salario = float(input("Digite seu salário: "))

if (salario <= 300):
    salario_final = salario * 1.35
    print("Com o reajuste de 35% seu salario ficou de",salario_final)

else:
    salario_final = salario *1.15
    print("Com o reajuste de 15% seu salario ficou de",salario_final)
