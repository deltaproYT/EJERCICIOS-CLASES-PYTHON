# Estudiante: Jordy Wladimir Ortiz Aquino
# Fecha: 30/06/2026
# Asignatura: Lenguaje de Programacion Python
# Proposito: Sistema de inventario de dispositivos de red.

# ---------------------------------------------------------------
# TIPO 1: FUNCION SUELTA  (fuera de cualquier clase)
# ---------------------------------------------------------------
def imprimir_banner():
    print("=" * 48)
    print("    SISTEMA DE INVENTARIO DE DISPOSITIVOS        ")
    print("=" * 48 + "\n")


# ---------------------------------------------------------------
# CLASE PRINCIPAL
# ---------------------------------------------------------------
class Dispositivo:

    def __init__(self, ip, modelo, ubicacion):
        self.modelo = modelo
        self.ubicacion = ubicacion
        self.ip = ip  # Llama al setter definido abajo

    # TIPO 3: @property (con validacion)
    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, valor):
        partes = valor.split('.')
        if len(partes) != 4:
            raise ValueError('IP invalida: ' + valor)

        for p in partes:
            if not p.isdigit() or not (0 <= int(p) <= 255):
                raise ValueError('IP invalida: ' + valor)

        self._ip = valor

    # TIPO 2: METODO NORMAL  (con self)
    def reportar(self):
        print(f"Dispositivo: {self.ip}")
        print(f"  Modelo:    {self.modelo}")
        print(f"  Ubicacion: {self.ubicacion}\n")

    # TIPO 4: @staticmethod  (sin self, sin cls)
    @staticmethod
    def es_ip_privada(ip):
        if ip.startswith('10.'):
            return True
        if ip.startswith('192.168.'):
            return True
        if ip.startswith('172.'):
            partes = ip.split('.')
            if len(partes) >= 2 and 16 <= int(partes[1]) <= 31:
                return True
        return False

    # TIPO 5: @classmethod  (constructor alternativo)
    @classmethod
    def desde_csv(cls, linea):
        ip, modelo, ubicacion = linea.split(',')
        return cls(ip.strip(), modelo.strip(), ubicacion.strip())


# ---------------------------------------------------------------
# PROGRAMA PRINCIPAL  (pruebas)
# ---------------------------------------------------------------
if __name__ == "__main__":
    imprimir_banner()

    dev1 = Dispositivo('10.0.0.1', 'Cisco-2960', 'DC-A')

    dev2 = Dispositivo.desde_csv('192.168.1.1, MikroTik, Oficina')

    dev1.reportar()
    dev2.reportar()

    print(f"10.0.0.5    es privada? {Dispositivo.es_ip_privada('10.0.0.5')}")
    print(f"8.8.8.8     es privada? {Dispositivo.es_ip_privada('8.8.8.8')}\n")

    try:
        d = Dispositivo('999.0.0.1', 'X', 'Y')
    except ValueError as e:
        print('Error capturado:', e)