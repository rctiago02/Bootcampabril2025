# Definir palabra a encontrar, intentos y la cantidad de letras
palabra_a_encontrar = "virus"
cantidad_de_letras = 5
intentos = 6



# Comparamos las palabras (posicion correcta, si existe en la palabra o si no existe)
def verificar_palabra_ingresada(palabra_a_encontrar, palabra_ingresada):




    # Definir una lista y agregar las letras verificadas
    resultado = []

    for posicion in range(cantidad_de_letras):
        las_letras_son_iguales = palabra_a_encontrar
        [posicion] == palabra_ingresada[posicion]

        la_letra_existe = palabra_ingresada[posicion] in palabra_a_encontrar

        if las_letras_son_iguales:
            #agregar la letras entre corchetes
            resultado.append('['+palabra_ingresada[posicion]+']')
        elif la_letra_existe:
            resultado.append('('+palabra_ingresada[posicion]+')')
        else:
            resultado.append(palabra_ingresada[posicion])
    return


grilla = []

# Hacer la grilla 

def imprimir_grilla():
    cantidad_de_filas = len(grilla)

    for fila in range(cantidad_de_filas):
        print(grilla[fila])



# Bienvenida al wordle

print("Bienvenido a Wordle")

# Restar la cantidad de intentos
while intentos > 0:
    print(f"te quedan {intentos}")
    palabra_ingresada = input("igresa la palabra")
    intentos = intentos - 1

    if len(palabra_ingresada) != cantidad_de_letras:
        print(f"ingrese una palabra con {cantidad_de_letras}")
        continue
    else:
        # verificamos la palabra
        linea_verificada = verificar_palabra_ingresada(palabra_a_encontrar,palabra_ingresada)
        grilla.append(linea_verificada)

    imprimir_grilla(grilla)
    if palabra_ingresada == palabra_a_encontrar:
        print("Ganaste!!!")
        break



