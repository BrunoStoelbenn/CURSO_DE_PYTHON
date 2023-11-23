import importlib

import aula98m

print(aula98m.nome)
print(aula98m.idade)
print(aula98m.altura)

for i in range(10):
    importlib.reload(aula98m)