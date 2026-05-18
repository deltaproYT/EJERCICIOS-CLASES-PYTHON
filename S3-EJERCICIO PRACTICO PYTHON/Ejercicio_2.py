puerto = int(input(' Ingrese el numero de puerto que desee conocer: '))

Num_Puerto = {
    22: 'SSH',
    80: 'HTTP',
    443: 'HTTPS',
    3306: 'MySQL',
    3389: 'RDP'
}

if puerto in Num_Puerto:
    print(Num_Puerto[puerto])
else:
    print(f'el puerto {puerto} es un puerto desconocido')