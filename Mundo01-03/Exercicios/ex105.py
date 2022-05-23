def notas(*nota, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param nota: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dicio = {}
    dicio['total'] = len(nota)
    dicio['maior'] = max(nota)
    dicio['menor'] = min(nota)
    dicio['média'] = sum(nota) / len(nota)
    if sit:
        if dicio['média'] >= 7:
            dicio['situação'] = 'BOA'
        elif dicio['média'] >= 5:
            dicio['situação'] = 'RAZOÁVEL'
        else:
            dicio['situação'] = 'RUIM'
    return dicio


resp = notas(3.5, 2, 6.5, 10, sit=True)
print(resp)
help(notas)
