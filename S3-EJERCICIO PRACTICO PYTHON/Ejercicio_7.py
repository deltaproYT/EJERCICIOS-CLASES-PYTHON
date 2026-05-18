puertos = [21, 22, 23, 25, 80]
estados = ["abierto", "abierto", "abierto", "cerrado", "abierto"]

for puertos, estados in zip(puertos, estados):
    if estados == "cerrado":
        print(f'Primer puerto cerrado: {puertos}')
        break
    else:
        print(f'Puerto {puertos}: {estados}')