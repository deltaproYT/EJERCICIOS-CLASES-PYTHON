from time import process_time_ns

inventario = ["Router-01", "Switch-A", "Firewall-FW1", "Servidor-Web"]
buscar = "Firewall-FW1"
encontrado = False

for dispositivo in inventario:
    if dispositivo == buscar:
        encontrado = True
        break


if encontrado:
    print(f'{buscar} Encontrado')
else:
    print('No encontrado en el inventario')
