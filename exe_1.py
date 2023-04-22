#Faça um programa que receba três notas de um aluno, calcule sua média final e diga se o mesmo está aprovado ou reprovado (se sua média for maior que 5, estará aprovado);

nota_1 = int(input("Digite a sua primeira nota: "))
nota_2 = int(input("Digite a sua segunda nota: "))
nota_3 = int(input("Digite a sua terceira nota: "))

media = (nota_1 + nota_2 + nota_3)/3

if (media > 5 ):
    print("Parabéns você foi aprovado, sua media foi de",media)
else:
    print("Infelismente você não conseguiu obter a media minima, sua media foi",media)
