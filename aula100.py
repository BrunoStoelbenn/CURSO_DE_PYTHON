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
    {**produto, 'preco': round(produto['preco'] * 1.1, 2)}
    for produto in produtos
]

produtos_ordenados_nome =  sorted(produtos, key=lambda produto: produto['nome'], reverse=True)
produtos_ordenados_preco =  sorted(produtos, key=lambda produto: produto['preco'])

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_nome, sep='\n')
print()
print(*produtos_ordenados_preco, sep='\n')

