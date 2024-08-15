set_inicial = {11, 12, 13, 14}

print("Conteúdo do set inicial:", set_inicial)

set_inicial.add(15)

print("Conteúdo do set após adicionar 15:", set_inicial)

set_inicial.update({1, 2, 3, 4, 5})

print("Conteúdo do set após update:", set_inicial)

set_inicial.discard(13)

print("Conteúdo do set após remover 13:", set_inicial)

novo_set = {20, 21, 23, 1, 2}

print("Conteúdo do novo set:", novo_set)

uniao_sets = set_inicial.union(novo_set)
print("Resultado da união dos sets:", uniao_sets)

intersecao_sets = set_inicial.intersection(novo_set)
print("Resultado da interseção dos sets:", intersecao_sets)

diferenca_sets = set_inicial.difference(novo_set)
print("Resultado da diferença dos sets (set_inicial - novo_set):", diferenca_sets)

diferenca_simetrica_sets = set_inicial.symmetric_difference(novo_set)
print("Resultado da diferença simétrica dos sets:", diferenca_simetrica_sets)