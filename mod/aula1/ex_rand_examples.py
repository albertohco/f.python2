"""Exemplos das funções do módulo random (pt-br).
Executar para ver saídas reproducíveis.
"""
import random
from random import randrange, randint, choice, choices, sample, shuffle, uniform

print("-- seed fixa -> sequências reproduzíveis --")
random.seed(123)
print("random():", random.random())
print("randrange(10):", randrange(10))
print("randrange(0,10):", randrange(0, 10))
print("randrange(0,10,2):", randrange(0, 10, 2))
print("randint(0,5):", randint(0, 5))
print("uniform(1.5, 3.5):", uniform(1.5, 3.5))
print("choice([a,b,c]):", choice(['a', 'b', 'c']))
print("choices([a,b,c], k=5):", choices(['a', 'b', 'c'], k=5))
print("sample(range(10), 4):", sample(range(10), 4))

lst = list(range(6))
print("shuffle antes:", lst)
shuffle(lst)
print("shuffle depois:", lst)

print("getrandbits(8):", random.getrandbits(8))

print('\n-- Random() instance (semente própria) --')
r = random.Random(7)  # gerador independente
print("r.random():", r.random())
print("r.randint(1,10):", r.randint(1, 10))

print('\n-- getstate/setstate (restaurar sequência) --')
random.seed(42)
print("A1:", random.random())
state = random.getstate()
print("A2:", random.random())
random.setstate(state)
print("A2 depois de restaurar state (deve ser igual à A2 original):", random.random())

print('\n-- Observações rápidas --')
print("seed(None) -> usa fonte do sistema (temporal)")
print("Para segurança criptográfica use module 'secrets' em vez de 'random'.")
