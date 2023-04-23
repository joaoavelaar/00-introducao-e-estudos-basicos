# Faça um programa que receba o preço de um produto, calcule e mostre, de acordo com as tabelas a seguir, o novo preço e a classificação;

preco_produto = float(input("Digite o preço: "))

if (preco_produto < 50):
    aumento_preco = preco_produto * 0.05

elif (preco_produto >= 50 and preco_produto <= 100):
    aumento_preco = preco_produto * 0.10

else: #Preço acima de 100
    aumento_preco = preco_produto * 0.15
novo_preco = preco_produto + aumento_preco
print("Novo preço: R$",novo_preco)

if (novo_preco < 80):
    print("Produto barato")

elif (novo_preco >= 80 and novo_preco <= 120):
    print("Produto razoável")

elif (novo_preco >= 120 and novo_preco <= 200):
    print("Produto caro")

else: # novo_preco> 200
    print("Produto muito caro")