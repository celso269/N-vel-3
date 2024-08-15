def calcular_media(notas):
    """
    Calcula a média das notas fornecidas.
    
    :param notas: Lista com as notas dos 4 bimestres.
    :return: Média das notas.
    """
    return sum(notas) / len(notas)

def verificar_reprovacao(media):
    """
    Verifica se a média é inferior a 6 (reprovado).
    
    :param media: Média das notas.
    :return: True se a média for inferior a 6, False caso contrário.
    """
    return media < 6

def alunos_reprovados(dados_alunos, matriculas_reprovados):
    """
    Retorna informações sobre os alunos reprovados.
    
    :param dados_alunos: Dicionário com informações dos alunos.
    :param matriculas_reprovados: Lista com as matrículas dos alunos reprovados.
    :return: Lista de strings com informações sobre os alunos reprovados.
    """
    reprovados = []
    for matricula in matriculas_reprovados:
        aluno = dados_alunos.get(matricula)
        if aluno:
            reprovados.append(
                f"Aluno Reprovado: {aluno['nome']} – Matrícula: {matricula} – Média Final: {aluno['media']:.2f}"
            )
    return reprovados

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