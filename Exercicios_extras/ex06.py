# ================================================
# SUPER DESAFIO – SISTEMA DE ESTOQUE
# -----------------------------------------------
# Crie um programa que simule o controle de um pequeno estoque.
# Requisitos:
# - Use um dicionário chamado 'estoque', onde as chaves são os nomes dos produtos
#   e os valores são as quantidades.
# - O programa deve ter um menu de opções (usando laço while):
#
#   1 - Adicionar produto
#   2 - Atualizar quantidade
#   3 - Remover produto
#   4 - Mostrar estoque
#   5 - Mostrar produtos com quantidade zero
#   6 - Sair
#
# - Utilize estruturas condicionais, loops e operações com dicionário/conjunto
#   quando fizer sentido.
# - O menu deve continuar até o usuário escolher “Sair”.
# ================================================

estoque = {}

while True:
    print("1 - Adicionar produto\n2 - Atualizar quantidade\n3 - Remover produto\n4 - Mostrar estoque\n5 - Mostrar produto com quantidade zero\n6 - Sair")
    menu = int(input("Escolha uma opção: "))

    if menu == 1:
        produto = input("Digite o nome do produto que irá adicionar: ").lower()
        qntd = int(input("Digite a quantidade desse produto: "))
        estoque.update({produto:qntd})
    elif menu == 2:
        produto = input("Digite o nome do produto que quer atualizar: ").lower()
        qntd = int(input("Digite a quantidade: "))
        estoque[produto] = qntd
    elif menu == 3:
        produto = input("Digite o nome do produto que quer remover: ").lower()
        del estoque[produto]
    elif menu == 4:
        print(f"Estoque = {estoque}")
    elif menu == 5:
        estoque_zero = []
        for key, value in estoque.items():
            if value == 0:
                estoque_zero.append(key)
        
        print(f"Produtos com estoque zero:\n{estoque_zero}")
    elif menu == 6:
        break
    else:
        continue