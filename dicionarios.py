meu_dicionario = {
    1: "Python",
    2: "Java",
    3: "PHP"
}

print("Conteúdo do dicionário:", meu_dicionario)

print("Tipo de dados de meu_dicionario:", type(meu_dicionario))

print("Valor da chave 1:", meu_dicionario.get(1))

print("Tamanho do dicionário:", len(meu_dicionario))

dicionario_frutas = {
    1: {"nome": "limão", "tipo": "ácida"},
    2: {"nome": "laranja", "tipo": "ácida"},
    3: {"nome": "manga", "tipo": "semiácida"},
    4: {"nome": "maçã", "tipo": "semiácida"},
    5: {"nome": "banana", "tipo": "doce"},
    6: {"nome": "mamão", "tipo": "doce"}
}
print("Chave 1 - Nome:", dicionario_frutas[1]["nome"], ", Tipo:", dicionario_frutas[1]["tipo"])

print("Chave 2 - Nome:", dicionario_frutas[2]["nome"], ", Tipo:", dicionario_frutas[2]["tipo"])

for chave, valor in dicionario_frutas.items():
    print(f"Chave {chave} - Nome: {valor['nome']}, Tipo: {valor['tipo']}")
