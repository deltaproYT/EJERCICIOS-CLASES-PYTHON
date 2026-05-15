# =============================================================================
#  CLASE - BUCLE FOR + CONTROLES (break / continue / pass / else)
#
#  Cada ejercicio esta dentro de su propia funcion. main() los llama en
#  orden. Comente las llamadas que NO vaya a ejecutar en clase.
# =============================================================================


# =============================================================================
#  NOTA TEORICA - BUCLE FOR
# =============================================================================
#  El for de Python NO es un contador como en Java/C. Recorre los elementos
#  de una secuencia (lista, cadena, range, tupla, diccionario, ...).
#
#  Sintaxis:
#     for <variable> in <secuencia>:
#         <bloque indentado>
#
#  Funciones auxiliares muy usadas:
#     range(N)            -> 0, 1, 2, ..., N-1
#     range(A, B)         -> A, A+1, ..., B-1   (B es EXCLUSIVO)
#     range(A, B, paso)   -> con incremento personalizado
#     enumerate(secuencia, start=0) -> entrega (indice, valor)
#     zip(lista1, lista2) -> recorre dos listas en paralelo
# =============================================================================


# =============================================================================
#  NOTA TEORICA - CONTROLES FINOS DEL BUCLE
# =============================================================================
#  Estas cuatro palabras clave modifican el comportamiento por defecto del for
#  (y tambien del while). Son su "control fino":
#
#     break     -> SALE del bucle inmediatamente.
#                  Cuando usarlo: ya encontre lo que buscaba, no tiene sentido
#                  seguir. Ejemplo: primer host caido, primera coincidencia.
#
#     continue  -> SALTA a la siguiente iteracion.
#                  Cuando usarlo: este elemento no me interesa, pero quiero
#                  seguir con los demas. Ejemplo: ignorar IPs de blacklist.
#
#     pass      -> NO HACE NADA. Es un marcador de posicion.
#                  Cuando usarlo: cuando Python exige un bloque pero todavia
#                  no quiero implementarlo (un "TODO" sintacticamente valido).
#
#     else      -> Se ejecuta SOLO si el bucle termino SIN haber pasado por
#                  un break. Util para reportar "no encontrado" sin usar
#                  banderas auxiliares. Esto NO existe en Java ni en C, es
#                  caracteristica unica de Python.
#
#  Tabla resumen rapida:
#     break    -> "salgo"
#     continue -> "salto este"
#     pass     -> "no hago nada (aun)"
#     else     -> "termine sin break"
# =============================================================================


def ejercicio_2_1():
    """For sobre una lista."""
    print("\n--- Ejercicio 2.1: Recorrer lista de servicios ---")
    # OBSERVACION: La variable "servicio" no existe antes del bucle. Python
    # la crea y le asigna cada elemento de la lista, uno a la vez.

    servicios = ["SSH", "HTTP", "HTTPS", "FTP", "DNS"]

    for recorrido in servicios:
        print(f"Verificando servicio: {recorrido}")


def ejercicio_2_2():
    """For con range() - contador numerico."""
    print("\n--- Ejercicio 2.2: Escaneo de rango de puertos ---")
    # OBSERVACION: range() se usa cuando si necesitamos numeros.
    #     range(20, 26) genera 20, 21, 22, 23, 24, 25  (el 26 NO se incluye).

    for puerto in range(20, 26):
        print(f"Probando puerto {puerto}...")

    # TECNICA: El limite superior de range() es SIEMPRE exclusivo.


def ejercicio_2_3():
    """For con enumerate() - indice + valor."""
    print("\n--- Ejercicio 2.3: Listado numerado de hosts ---")
    # OBSERVACION: enumerate() devuelve tuplas (indice, valor). Python las
    # desempaqueta automaticamente en las dos variables del for.

    lista_host = ["10.0.0.1", "10.0.0.2", "10.0.0.3", "10.0.0.4"]

    for indice, valor in enumerate(lista_host, start=1):
        print(f"Host #{indice}: {valor}")


def ejercicio_2_4():
    """For con zip() - dos listas en paralelo."""
    print("\n--- Ejercicio 2.4: Tabla de puerto-servicio ---")
    # OBSERVACION: zip() empareja listas elemento por elemento. Si una es
    # mas corta, zip se detiene al agotarla.

    puertos   = [90, 22, 80, 443, 3306, 3389]
    servicios = ["DESCONOCIDO", "SSH", "HTTP", "HTTPS", "MySQL", "RDP"]

    for puerto, servicio in zip(puertos, servicios):
        print(f"Puerto {puerto:>5}  ->  {servicio}")

    # FORMATO: ":>5" alinea a la derecha en un ancho de 5 caracteres.


def ejercicio_2_5():
    """For sobre una cadena (string)."""
    print("\n--- Ejercicio 2.5: Recorrer una contrasena ---")
    # OBSERVACION: Las cadenas tambien son secuencias. Cada iteracion
    # entrega UN caracter.

    contrasena = "Admin@123"
    contador_simbolos = 0

    for caracter in contrasena:
        print(f"Caracter: '{caracter}'")
        if not caracter.isalnum():
            contador_simbolos += 1

    print(f"La contrasena tiene {contador_simbolos} simbolo(s) especial(es)")

    # DIDACTICA: for + if + contador es el patron mas usado en analisis
    # de datos.


# =============================================================================
#  CONTROLES FINOS DEL BUCLE
# =============================================================================

def control_break():
    """break - SALE del bucle apenas se cumple la condicion."""
    print("\n--- Control: break (salir del bucle) ---")
    # CUANDO USARLO: Cuando ya conseguimos el resultado y seguir iterando
    # seria un desperdicio. Tipico en busquedas.

    ips     = ["10.0.0.1", "10.0.0.2", "10.0.0.3", "10.0.0.4"]
    estados = [True,        True,        False,       True]

    for ip, activa in zip(ips, estados):
        if not activa:
            print(f"Primer host caido detectado: {ip}")
            break              # SALIMOS - no revisamos los demas
        print(f"  {ip}: OK")

    print(f"Salida")
    # COMO FUNCIONA: Al ejecutarse break, se interrumpe el bucle y la
    # ejecucion continua DESPUES del for. No se hacen mas iteraciones.


def control_continue():
    """continue - SALTA al siguiente elemento."""
    print("\n--- Control: continue (saltar elemento) ---")
    # CUANDO USARLO: Cuando este elemento no me interesa pero quiero
    # seguir procesando los demas. Filtros, exclusiones, blacklists.

    for puerto in range(20, 30):
        if puerto % 2 != 0:    # si es impar...
            continue           # ...saltar a la siguiente iteracion
        print(f"Puerto par: {puerto}")

    # COMO FUNCIONA: continue NO rompe el bucle, solo ignora lo que
    # quedaba debajo en esa iteracion y pasa a la siguiente.
    # TECNICA: % es el operador residuo. "n % 2 != 0" -> n es impar.


def control_else_de_bucle():
    """else del for - se ejecuta SOLO si NO hubo break."""
    print("\n--- Control: else del for (sin break = no encontrado) ---")
    # CUANDO USARLO: En busquedas, para reportar "no se encontro" sin
    # tener que crear una bandera (flag) auxiliar.

    ip_buscada = "10.0.0.99"
    ips = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]

    for ip in ips:
        if ip == ip_buscada:
            print(f"IP {ip_buscada} encontrada")
            break
    else:
        # Este else pertenece al FOR, no a un if. Se ejecuta solo si el
        # for termino normalmente (sin haber pasado por break).
        print(f"IP {ip_buscada} no esta en la lista")

    # COMO FUNCIONA:
    #   - Si hubo break  -> NO se ejecuta el else.
    #   - Si NO hubo break (recorrio todo) -> SI se ejecuta el else.


def control_pass():
    """pass - marcador de posicion, no ejecuta nada."""
    print("\n--- Control: pass (placeholder sintactico) ---")
    # CUANDO USARLO: Cuando Python exige un bloque pero aun no quiero
    # poner codigo. Es un "TODO" valido sintacticamente.

    usuarios = ["admin", "invitado", "root", "soporte"]

    for usuario in usuarios:
        if usuario == "root":
            pass
        else:
            print(f"Usuario procesado: {usuario}")

    # COMO FUNCIONA: pass es literalmente "no hacer nada". Si lo quito,
    # el if quedaria vacio y Python lanzaria IndentationError.



# =============================================================================
#  MAIN
# =============================================================================
print("=" * 60)
print("CLASE - SEMANA 3 - PARTE 2: BUCLE FOR + CONTROLES")
print("=" * 60)

# --- For basico ---
# ejercicio_2_1()
# ejercicio_2_2()
# ejercicio_2_3()
# ejercicio_2_4()
# ejercicio_2_5()
#
# # --- Controles finos ---
# control_break()
# control_continue()
# control_else_de_bucle()
control_pass()




