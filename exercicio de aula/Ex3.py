# Lista de nomes fornecida
nomes = [
    "Pedro Pereira",
    "Ana Beatriz",
    "Ana Clara",
    "Carlos Silva",
    "Beatriz Souza",
    "Ana Paula",
    "Pedro Andrade"
]

# Ordena a lista de nomes
# A "key" extrai o primeiro nome e o apelido para criar uma tupla
# Python ordena a tupla primeiro pelo primeiro item (primeiro nome)
# e, em caso de empate, usa o segundo item (apelido) como critério de desempate
nomes.sort(key=lambda nome: (nome.split()[0], nome.split()[1]))

# Exibe o resultado final
print("Lista de Nomes Ordenada:")
for nome in nomes:
    print(f"{nome}")

