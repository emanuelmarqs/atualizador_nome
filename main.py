nomes = ['Emanuel', 'Fernanda', 'Carlos', 'Carlota', 'Natalia', 'Emanuel']

#usuário informa o índice que deseja alterar
indice = int(input('Informe o índice que deseja alterar algum entre 1-6: '))
indice -= 1

# usuário informa o novo nome
nomes[indice] = input('Informe o novo nome:  ')

#exibe a lista
for nome in nomes:
    print(nome)

