# Faça um programa que lê o número de gols marcados pelo Flamengo e o número de gols marcados pelo Vasco. Escrever o nome do time vencedor. Caso não haja vencedor, escrever EMPATE

gols_flamengo = int(input ("Digite un número de gols do flamengo:"))
gols_vasco = int(input("Digite um número de gols do vasco: "))

if (gols_flamengo > gols_vasco):
    print ("Flamengo é vencedor com o total de",gols_flamengo, "gols")

elif (gols_vasco > gols_flamengo):
    print("Vasco é vencedor com o total de", gols_vasco,"gols")

else:
    print("Deu empate")
