def get_response(number):
    if number == 3:
        return True

intento = 0
while intento < 5:
    intento += 1
    if get_response(intento):
        print(f'Intento {intento}: CONECTADO')
        break
    else:
        print(f'Intento {intento}: Sin Respuesta')

