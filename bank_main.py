# Lista de usuários
usuarios = ["thiago", "john"]
senhas = [2112, 1707]

# Mensagem de boas-vindas
print('Olá, bem-vindo ao Banco Itacu')
print('Digite o número da sua conta e sua senha')

# Receber o nome do usuário
acesso_nome = input("Digite seu usuário: ").strip().lower()
acesso_senha = int(input("Digite sua senha: ").strip())

# Verificando usuario
if acesso_nome in usuarios:
    # Encontrando o índice do usuário na lista
    indice = usuarios.index(acesso_nome)
    
    # Verificando se a senha correspondente está correta
    if senhas[indice] == acesso_senha:
        print('Acesso permitido')
    else:
        print('Senha incorreta')
else:
    print("Usuário não encontrado.")

print("Bem vindo {}, o que gostaria de fazer? ".format(acesso_nome))
print("Sacar, Extrato ou Depositar")