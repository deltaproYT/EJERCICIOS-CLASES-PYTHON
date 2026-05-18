protocolo = input('Ingrese el protocolo que desee: ')

def string_mayus(palabra):
    return palabra.upper()

seguros = [
    'HTTPS',
    'SSH',
    'SFTP'
]

inseguros = [
    'HTTP',
    'TELNET',
    'FTP'
]

if string_mayus(protocolo) in seguros:
    print(f'El protocolo {protocolo} esta seguro')

elif string_mayus(protocolo) in inseguros:
    print(f'El protocolo {protocolo} esta inseguro')

else:
    print(f'El protocolo {protocolo} es desconocido')