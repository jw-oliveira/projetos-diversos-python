class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ['Basic', 'Premium']
        
        if plano in self.lista_planos:
            self.plano = plano
        else:
            print('Plano inválido')

    
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print('Plano inválido')

    
    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f'Ver Filme {filme}')
        elif self.plano == 'Premium':
            print(f'Ver filme {filme}')
        elif self.plano == 'Basic' and plano_filme == 'Premium':
            print('Faça upgrade para o Plano Premium')
        else:
            print('Plano inválido')


# Primeiro cadastro
cliente1 = Cliente('Jorge', 'jorge@mail.com', 'Basic')
print(cliente1.plano)
cliente1.ver_filme('Harry Potter', 'Premium')

# Upgrade
cliente1.mudar_plano('Premium')
print(cliente1.plano)
cliente1.ver_filme('Harry Potter', 'Premium')
