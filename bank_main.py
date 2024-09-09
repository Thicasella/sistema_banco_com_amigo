import os 
import getpass

# Lista de usuários e senhas
usuarios = ["thiago", "john"]
senhas = [2112, 1707]
valor = [2500.00, 3500.00]

# Mensagem de boas-vindas
print('Olá, bem-vindo ao Banco Itacu')
print('Digite o número da sua conta e sua senha')

# Inicializa as variáveis de acesso
acesso_nome = ""
acesso_senha = 0


while True:
    acesso_nome = input("Digite seu usuário: ").strip().lower()
    acesso_senha = getpass.getpass("Digite sua senha: ").strip()
    #acesso_senha = int(input("Digite sua senha: ").strip())
    
    # Convertendo a senha para inteiro para comparação
    acesso_senha = int(acesso_senha)

    # Verificando se o usuário existe na lista
    if acesso_nome in usuarios:
        # Encontrando o índice do usuário na lista
        indice = usuarios.index(acesso_nome)
        
        # Verificando se a senha correspondente está correta
        if senhas[indice] == acesso_senha:
            print('Acesso permitido')
            break 
        else:
            print('Senha incorreta. Tente novamente.')
    else:
        print("Usuário não encontrado. Tente novamente.")

# Continuar o fluxo após o login bem-sucedido
print("Bem vindo(a) {}, o que gostaria de fazer? ".format(acesso_nome))

entrada = int(input('1 para sacar\n2 para saldo\n3 para depositar \n0 para sair\nDigite seu escolha: '))

def saldo():
    os.system("cls")
    print('Você selecionou saldo ')
    print('Olá, senhor(a) {}, seu saldo é R${}'.format(acesso_nome, valor[indice]))

def saque():
    os.system("cls")
    print('Você selecionou sacar ')
    saque= float(input(print('Quanto você deseja sacar? : ')))
    novo_saldo =  valor[indice] - saque
    print('Você sacou {}, seu saldo atual é {}'.format(saque, novo_saldo))
    #valor[indice] += saque

def deposito():
    os.system("cls")
    print('Você escolheu depositar')
    depositar= float(input(print('quanto você deseja depositar? : ')))
    novo_deposito =  valor[indice] + depositar
    print('Você depositou {}, seu saldo atual é {}'.format(depositar, novo_deposito))
    #valor[indice] += depositar

if entrada == 1:
    saque()

elif entrada == 2:
    saldo()

elif entrada == 3:
    deposito()

elif entrada == 0:
    print('Você selecionou sair')
    print('Ate mais Sr.(a) {}'.format(acesso_nome))
    exit()
else:
    print('Não existe essa opção')
