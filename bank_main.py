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
    acesso_senha = int(input("Digite sua senha: ").strip())
    
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
print("Bem vindo {}, o que gostaria de fazer? ".format(acesso_nome))
print("Sacar, Extrato ou Depositar")

entrada = int(input('digite 1 para sacar, 2 para extrato e 3 para depositar: '))

if entrada == 1:
    print('Você selecionou sacar')
    saque= float(input(print('quanto vc deseja sacar? :')))
    novosaldo =  valor[indice] - saque
    print('voce sacou {}, seu saldo atual é {}'.format(saque, novosaldo))
elif entrada == 2:
    print('Você selecionou saldo')
    print('olá, senhor {}, seu estrato é R${}'.format(acesso_nome, valor[indice]))
elif entrada == 3: 
    print('Você escolheu depositar')
else:
    print('Não existe essa opção')