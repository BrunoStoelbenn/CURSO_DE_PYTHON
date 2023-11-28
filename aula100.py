from dados import produtos
# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.1}
    for produto in produtos
]

produtos_ordenados_nome =  sorted(produtos, key=lambda item: item['nome'])
produtos_ordenados_preco =  sorted(produtos, key=lambda item: item['preco'])

print(produtos)
print()
print(novos_produtos)
print()
print(produtos_ordenados_nome)
print()
print(produtos_ordenados_preco)

