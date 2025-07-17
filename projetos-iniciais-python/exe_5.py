# Um determinado clube de futebol pretende classificar seus atletas em categorias. Para isso, o clube contratou você para criar um programa que executasse essa tarefa. Baseada na tabela de categorias do clube, construa  um programa que solicite a idade de um atleta e imprima sua categoria;

idade = int(input("Digite sua idade: "))

if (idade >= 5 and idade <= 10):
    print ("Sua categoria é infantil")

if (idade >= 11 and idade <= 15):
    print ("Sua categoria é juvenil")

if (idade >= 16 and idade <= 20):
    print ("Sua categoria é junior")

if (idade >= 21 and idade <= 25):
    print ("Sua categoria é profissional")

else:
    print("Você não se encaixa nas categorias!! ")
