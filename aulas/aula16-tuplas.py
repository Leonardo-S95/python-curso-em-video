# Variáveis simples armazenam somente um valor. Variáveis compostas podem armazenar vários valores.
# Toda variável simples é um espaço na memória.
# Tuplas são imutáveis.

# lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

# for comida in lanche:
#     print(f'Eu vou comer {comida}')

# Se precisar da posição do dado, olhe as opções abaixo.

# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]} na posição {cont}')

# for pos,comida in enumerate(lanche):
#    print(f'Eu vou comer {comida} na posição {pos}')

# Os dois métodos acima printam a mesma coisa.

# print(sorted(lanche))       # sorted coloca em ordem.

# a = (2, 5, 4)
# b = (5, 8, 1, 2)
# c = b + a

# print(c)
# print(c.index(2, 4))   # mostra a primeira posição em que o elemento pedido(2) aparece.
                       # Pode colocar vírgula e adicionar uma posição(4) para se começar.
# print(c.count(5))   # conta a quantia de numero 5 na tupla.

pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa)         # del = deletar
print(pessoa)
