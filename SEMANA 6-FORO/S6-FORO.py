def validar_ip(ip):
    Octetos = ip.split('.')
    if len(Octetos) != 4:
        raise ValueError('La IP no tiene 4 octetos')
    for Num in Octetos:
        if not Num.isdigit():
            raise ValueError('El valor no es un numero entero')
        if int(Num) < 0 or int(Num) > 255:
            raise ValueError('El valor no se encuentra en el rango de 0-255')

    return ip

class Dispositivo:
    def __init__(self, nombre, ip):
        self.nombre = nombre
        self.ip = validar_ip(ip)
        self.estado = False

    def toggle_status(self):
        self.estado = not self.estado
        if self.estado:
            print('Encendiendo Dispositivo...\n')
        else:
            print('Apagando Dispositivo...\n')

    def show_data(self):
        if self.estado:
            print(f"DATOS DEL DISPOSITIVO\n\nNombre: {self.nombre} \nIP:{self.ip}\n")
        else:
            raise Exception('El dispositivo se encuentra apagado')


if '__main__' == __name__:
    Router_Cisco = Dispositivo('Route Cisco', '192.168.1.1')
    try:
        Router_Cisco.show_data() #Trata de mostrar datos estando apagado (Error)
    except Exception as e:
        print(f'ERROR!: "{e}"\n')

    Router_Cisco.toggle_status()
    Router_Cisco.show_data()
    Router_Cisco.toggle_status()
    try:
        Dispositivo_Falso= Dispositivo('Dispositivo_Falso', '999.abc.1.')
        Dispositivo_Falso.toggle_status()
        Dispositivo_Falso.show_data()
    except Exception as e:
        print(f'ERROR!: "{e}"\n')