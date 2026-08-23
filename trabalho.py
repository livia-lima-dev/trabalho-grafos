import matplotlib.pyplot as plt

#Vertices
V = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO",
    "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI",
    "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO" ]

#Arestas
E = [
    ("AC", "AM"),
    ("AC", "RO"),

    ("AL", "BA"),
    ("AL", "PE"),
    ("AL", "SE"),

    ("AP", "PA"),

    ("AM", "MT"),
    ("AM", "PA"),
    ("AM", "RO"),
    ("AM", "RR"),

    ("BA", "ES"),
    ("BA", "GO"),
    ("BA", "MG"),
    ("BA", "PE"),
    ("BA", "PI"),
    ("BA", "SE"),
    ("BA", "TO"),

    ("CE", "PB"),
    ("CE", "PE"),
    ("CE", "PI"),
    ("CE", "RN"),

    ("DF", "GO"),
    ("DF", "MG"),

    ("ES", "MG"),
    ("ES", "RJ"),

    ("GO", "MG"),
    ("GO", "MS"),
    ("GO", "MT"),
    ("GO", "TO"),

    ("MA", "PA"),
    ("MA", "PI"),
    ("MA", "TO"),

    ("MT", "MS"),
    ("MT", "PA"),
    ("MT", "RO"),
    ("MT", "TO"),

    ("MS", "PR"),
    ("MS", "SP"),
    ("MS", "MG"),

    ("MG", "RJ"),
    ("MG", "SP"),

    ("PA", "RR"),
    ("PA", "RO"),
    ("PA", "TO"),

    ("PB", "PE"),
    ("PB", "RN"),

    ("PR", "SC"),
    ("PR", "SP"),

    ("PE", "PI"),

    ("PI", "TO"),

    ("RJ", "SP"),

    ("RS", "SC"),
    ]

#Criar lista de adjacência
def criar_lista_adjacencia(V, E):
    lista_adjacencia = {}

    for vertice in V:
        lista_adjacencia[vertice] = []

    for origem, destino in E:
        lista_adjacencia[origem].append(destino)
        lista_adjacencia[destino].append(origem)

    return lista_adjacencia

lista_adjacencia = criar_lista_adjacencia(V, E)

print("LISTA DE ADJACÊNCIA")

for vertice in V:
    print(vertice, "->", lista_adjacencia[vertice])

#Criar matriz de adjacência
def criar_matriz_adjacencia(V, E):
    n = len(V)

    matriz = [[0 for _ in range(n)] for _ in range(n)]

    indice = {}

    for i in range(n):
        indice[V[i]] = i

    for origem, destino in E:
        i = indice[origem]
        j = indice[destino]

        matriz[i][j] = 1
        matriz[j][i] = 1

    return matriz

matriz_adjacencia = criar_matriz_adjacencia(V, E)

print("\nMATRIZ DE ADJACÊNCIA")

print("     " + " ".join(f"{uf:>1}" for uf in V))

for i in range(len(V)):
    print(f"{V[i]:>3}  " + " ".join(f"{valor:>2}" for valor in matriz_adjacencia[i]))

#Criar lista indexada
def criar_lista_indexada(V, lista_adjacencia):
    alfa = []
    beta = []

    for vertice in V:
        alfa.append(len(beta))

        for vizinho in lista_adjacencia[vertice]:
            beta.append(vizinho)

    return alfa, beta

alfa, beta = criar_lista_indexada(V, lista_adjacencia)

print("\nLISTA INDEXADA")

print("Alfa:")
for i in range(len(V)):
    print(V[i], "->", alfa[i])

print("\nBeta:")
print(beta)

#Calcular grau de cada vértice
def calcular_graus(V, lista_adjacencia):
    graus = {}

    for vertice in V:
        graus[vertice] = len(lista_adjacencia[vertice])

    return graus

graus = calcular_graus(V, lista_adjacencia)

print("\nGRAUS DOS VÉRTICES")

for vertice in V:
    print(vertice, "->", graus[vertice])

#Encontrar maior e menor grau
grau_maximo = max(graus.values())
grau_minimo = min(graus.values())

#Encontrar empates
ufs_grau_maximo = [
    vertice for vertice in V
    if graus[vertice] == grau_maximo
]

ufs_grau_minimo = [
    vertice for vertice in V
    if graus[vertice] == grau_minimo
]

print("\nGRAU MÁXIMO")
print("Grau:", grau_maximo)
print("UFs:", ", ".join(ufs_grau_maximo))

print("\nGRAU MÍNIMO")
print("Grau:", grau_minimo)
print("UFs:", ", ".join(ufs_grau_minimo))

#Listar os vizinhos das UFs que têm grau máximo e mínimo
print("\nVIZINHOS DO GRAU MÁXIMO")

for vertice in ufs_grau_maximo:
    print(vertice, "->", ", ".join(lista_adjacencia[vertice]))


print("\nVIZINHOS DO GRAU MÍNIMO")

for vertice in ufs_grau_minimo:
    print(vertice, "->", ", ".join(lista_adjacencia[vertice]))

#Calcular frequência de cada grau
from collections import Counter

frequencia_graus = Counter(graus.values())

print("\nFREQUÊNCIA DOS GRAUS")

for grau in sorted(frequencia_graus):
    print(f"Grau {grau}: {frequencia_graus[grau]} UF(s)")

#Histograma
graus_x = list(sorted(frequencia_graus.keys()))
frequencias_y = [frequencia_graus[grau] for grau in graus_x]

plt.bar(graus_x, frequencias_y)

plt.xlabel("Grau")
plt.ylabel("Frequência")
plt.title("Frequência dos graus das UFs")

plt.xticks(graus_x)

plt.show()