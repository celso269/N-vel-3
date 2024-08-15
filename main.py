
from operacoes import calcular_media, verificar_reprovacao, alunos_reprovados

dados_alunos = {
    26: {'nome': 'Maria', 'notas': [8, 7, 5, 9]},
    101: {'nome': 'Ana', 'notas': [9, 9, 8, 9]},
    13: {'nome': 'João', 'notas': [6, 5, 5, 5]},
    37: {'nome': 'Ágatha', 'notas': [8, 6, 7.5, 9]},
    72: {'nome': 'Joaquim', 'notas': [6, 5.5, 5, 7]},
    5: {'nome': 'Félix', 'notas': [10, 8, 8, 8]}
}

for matricula, dados in dados_alunos.items():
    media = calcular_media(dados['notas'])
    dados['media'] = media

matriculas_reprovados = [matricula for matricula, dados in dados_alunos.items() if verificar_reprovacao(dados['media'])]

lista_reprovados = alunos_reprovados(dados_alunos, matriculas_reprovados)

for info in lista_reprovados:
    print(info)