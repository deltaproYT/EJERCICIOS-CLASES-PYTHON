# =============================================================================
#  CLASE - BUCLE WHILE
#
#  Cada ejercicio esta dentro de su propia funcion. main() los llama en
#  orden. Comente las llamadas que NO vaya a ejecutar en clase.
# =============================================================================


# =============================================================================
#  NOTA TEORICA - BUCLE WHILE
# =============================================================================
#  while se repite MIENTRAS una condicion sea verdadera.
#
#  Sintaxis:
#     while <condicion>:
#         <bloque indentado>
#
#  Cuando usar while (y no for):
#     - Cuando NO sabemos cuantas iteraciones haran falta.
#     - Cuando dependemos de una entrada externa (usuario, sensor, red).
#     - Cuando esperamos que algo cambie (timeout, conexion, respuesta).
#
#  Regla critica:
#     La variable de control DEBE cambiar dentro del bucle. Si no, el bucle
#     se vuelve INFINITO y bloquea el programa. Este es el error mas comun.
#
#  Controles finos validos tambien dentro de while:
#     break    -> sale del while.
#     continue -> salta al inicio (vuelve a evaluar la condicion).
#     else     -> se ejecuta si el while termino por condicion falsa (sin break).
# =============================================================================


def ejercicio_3_1():
    """While con condicion compuesta."""
    print("\n--- Ejercicio 3.1: Reintento de conexion ---")
    # OBSERVACION: La condicion combina DOS variables con "and". El bucle
    # sigue mientras: aun queden intentos Y no estemos conectados.

    intento = 1
    maximo_intentos = 5
    conectado = False

    while intento <= maximo_intentos and not conectado:
        print(f"Intento de conexion #{intento}...")

        if intento == 3:
            # conectado = True
            print("  -> Conexion exitosa!")

        intento += 1   # CRITICO: actualizar la variable de control

    if not conectado:
        print("No se pudo establecer conexion despues de los reintentos")

    # TECNICA: Si olvidamos "intento += 1", el bucle nunca termina.
    # Este es el error mas comun con while.


def ejercicio_3_2():
    """While para validacion de entrada (input)."""
    print("\n--- Ejercicio 3.2: Validacion de entrada ---")
    print("(Comentado para ejecucion automatica - descomentar en clase)")
    # OBSERVACION: while es perfecto para validar entradas. Seguimos
    # pidiendo el dato hasta que sea valido. Si nunca lo es, no salimos.

    # edad = -1
    # while edad < 0 or edad > 120:
    #     entrada = input("Ingrese su edad: ")
    #     if entrada.isdigit():
    #         edad = int(entrada)
    #     else:
    #         print("Debe ingresar un numero")
    # print(f"Edad registrada: {edad}")


def ejercicio_3_3():
    """while True + break - bucle infinito controlado."""
    print("\n--- Ejercicio 3.3: Menu interactivo ---")
    print("(Comentado para ejecucion automatica - descomentar en clase)")
    # OBSERVACION: A veces queremos un bucle infinito a proposito.
    # Tipico en servidores que escuchan hasta recibir orden de salida.
    # La salida se hace con "break" desde dentro del bucle.
    #
    # ESTE ES EL UNICO LUGAR DONDE break ES TAN IMPORTANTE EN WHILE:
    # sin break, "while True" jamas termina.

    # while True:
    #     print("\n=== MENU ===")
    #     print("1. Ver estado")
    #     print("2. Reiniciar servicio")
    #     print("3. Salir")
    #     opcion = input("Eleccion: ")
    #
    #     if opcion == "1":
    #         print("Estado: OK")
    #     elif opcion == "2":
    #         print("Reiniciando...")
    #     elif opcion == "3":
    #         print("Adios!")
    #         break    # UNICA forma de salir del while True
    #     else:
    #         print("Opcion invalida")


print("=" * 60)
print("CLASE - SEMANA 3 - PARTE 3: BUCLE WHILE")
print("=" * 60)

ejercicio_3_1()
# ejercicio_3_2()
# ejercicio_3_3()
