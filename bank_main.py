import os
import getpass

# Lista de usuários, senhas e valores
usuarios = ["thiago", "john"]
senhas = [2112, 1707]
valor = [2500.00, 3500.00]

# Inicializa as variáveis de acesso
acesso_nome = ""
acesso_senha = 0
indice = -1  # Variável para armazenar o índice do usuário


def exibir_opcoes():
    os.system("cls")
    print("Bem-vindo(a) {}, o que gostaria de fazer? ".format(acesso_nome))
    entrada = int(input('1 para sacar\n2 para saldo\n3 para depositar\n0 para sair\nDigite sua escolha: '))
    
    if entrada == 1:
        saque()
    elif entrada == 2:
        saldo()
    elif entrada == 3:
        deposito()
    elif entrada == 0:
        print('Você selecionou sair.')
        print('Até mais, Sr.(a) {}'.format(acesso_nome))
        exit()
    else:
        print('Opção inválida.')
        main()  # Volta ao menu principal se a opção for inválida


def saldo():
    os.system("cls")
    print('Você selecionou saldo.')
    print('Olá, senhor(a) {}, seu saldo é R${:.2f}'.format(acesso_nome, valor[indice]))
    input("\nPressione Enter para voltar ao menu.")
    main()  # Retorna ao menu principal após exibir o saldo


def saque():
    os.system("cls")
    print('Você selecionou sacar.')
    saque_valor = float(input('Quanto você deseja sacar? : '))
    
    if saque_valor > valor[indice]:
        print('Saldo insuficiente.')
    else:
        valor[indice] -= saque_valor  # Atualizando o saldo na lista
        print('Você sacou R${:.2f}, seu saldo atual é R${:.2f}'.format(saque_valor, valor[indice]))
    
    input("\nPressione Enter para voltar ao menu.")
    main()  # Retorna ao menu principal após o saque


def deposito():
    os.system("cls")
    print('Você selecionou depositar.')
    deposito_valor = float(input('Quanto você deseja depositar? : '))
    
    valor[indice] += deposito_valor  # Atualizando o saldo na lista
    print('Você depositou R${:.2f}, seu saldo atual é R${:.2f}'.format(deposito_valor, valor[indice]))
    
    input("\nPressione Enter para voltar ao menu.")
    main()  # Retorna ao menu principal após o depósito


def main():
    os.system("cls")
    exibir_opcoes()


# Loop de autenticação
while True:
    acesso_nome = input("Digite seu usuário: ").strip().lower()
    acesso_senha = int(input("Digite sua senha: ").strip())
    
    # Verificando se o usuário existe na lista
    if acesso_nome in usuarios:
        # Encontrando o índice do usuário na lista
        indice = usuarios.index(acesso_nome)
        
        # Verificando se a senha correspondente está correta
        if senhas[indice] == acesso_senha:
            print('Acesso permitido.')
            main()  # Chamando o menu principal após autenticação
            break
        else:
            print('Senha incorreta. Tente novamente.')
    else:
        print("Usuário não encontrado. Tente novamente.")
