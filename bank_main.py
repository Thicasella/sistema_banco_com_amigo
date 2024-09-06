# Lista de usuários
usuario = ["thiago", "jojho"]

# Mensagem de boas-vindas
print('Olá, bem-vindo ao Banco Itacu')
print('Digite o número da sua conta e sua senha')

# Receber o nome do usuário
acesso_nome = input("Digite seu usuário: ")

# Verificar se o nome está na lista de usuários permitidos
if acesso_nome in usuario:
    print('Acesso permitido')
else:
    print('Acesso negado, esse usuário não existe')


