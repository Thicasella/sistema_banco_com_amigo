class restaurante:
        nome = ''
        categoria= ''
        ativo = False


class pessoa:
        nome= ''
        cpf = ''
        idade = int





restaurante_praca = restaurante()
restaurante_praca.nome = 'praca'
restaurante_praca.categoria= 'gourmet'

restaurante_pizza = restaurante()
restaurante_pizza.nome = 'pizzaria Casella'
restaurante_pizza.categoria = 'italiana'

print(vars(restaurante_praca))
print(vars(restaurante_pizza))



            


