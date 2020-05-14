'''
            DESAFIO 105
Faça um programa que tenha uma função chamada notas() que pode receber várias notas de
alunos e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings da função.
'''


def notas(* n, sit=False):
    """
     -> Função para avaliar várias notas e situação da turma.
    :param n: Uma ou mais notas.
    :param sit: Mostrar, caso True, a situação da turma (opcional).
    :return: Dicionário com informações da turma.
    """
    dados = {}
    count = 0
    maior = menor = soma = 0

    for i in range(0, len(n)):
        count += 1
        soma += n[i]
        if i == 0:
            maior = n[i]
            menor = n[i]
        elif n[i] > maior:
            maior = n[i]
        elif n[i] < menor:
            menor = n[i]

    dados['total'] = count
    dados['maior'] = maior
    dados['menor'] = menor
    dados['média'] = soma / count

    if sit == True:
        if dados['média'] >= 7:
            dados['situação'] = 'BOA 06!'
        elif 7 > dados['média'] >= 5:
            dados['situação'] = 'Nhé'
        else:
            dados['situação'] = 'Estudar mais precisa o senhor!'

    return dados


# Programa principal
resp = notas(3.5, 10, 6.5, 9, 2, 4.5, 6, 10, sit=True)
print(resp)


'''
# SOLUÇÃO CURSO EM VÍDEO

def notas(* n, sit=False):
    """
     -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várioas informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)

    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


# Programa Proncipal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
'''
