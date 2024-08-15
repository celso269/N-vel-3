meu_dicionario = {
    1: {'nome': 'Maria', 'idade': 26, 'nacionalidade': 'brasileira'}
}

meu_dicionario.update({
    2: {'nome': 'João', 'idade': 30, 'nacionalidade': 'português'},
    3: {'nome': 'Ana', 'idade': 22, 'nacionalidade': 'espanhola'}
})

print("Dicionário atualizado:", meu_dicionario)

copia_dicionario = meu_dicionario.copy()

removido_pop = meu_dicionario.pop(2)
print("Elemento removido com pop:", removido_pop)
print("Conteúdo do dicionário após pop:", meu_dicionario)

removido_popitem = meu_dicionario.popitem()
print("Elemento removido com popitem:", removido_popitem)
print("Conteúdo do dicionário após popitem:", meu_dicionario)

meu_dicionario.clear()
copia_dicionario.clear()

novas_chaves = [4, 5, 6]
valor_padrao = "valor padrão"
novo_dicionario = dict.fromkeys(novas_chaves, valor_padrao)

print("Conteúdo do novo dicionário (items):", novo_dicionario.items())

print("Chaves do novo dicionário (keys):", novo_dicionario.keys())

print("Valores do novo dicionário (values):", novo_dicionario.values()) 