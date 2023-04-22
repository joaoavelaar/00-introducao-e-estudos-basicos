# Faça um programa que verifica a validade de uma senha fornecida pelo usuário. Se o usuário digitar a senha ‘123456’, escrever a mensagem ‘Acesso liberado’. Caso contrário, escrever ‘Acesso negado’;

usuario =  input("Digite seu email: ")
senha = input("Digite sua senha: ")

if (senha == '123456'):
    print("Acesso liberado,aguarde... ")
else:
    print("Acesso negado, tente novamente ")