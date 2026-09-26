"""/*
 * Crea un programa se encargue de transformar un número
 * entero a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */"""



def convertidor_binario():

    binario = []

    dividendo = int(input("Ingresa cualquier número entero: "))

    while dividendo !=0:
        residuo = dividendo % 2
        binario.append(residuo)
        dividendo = dividendo // 2

    print(binario[::-1])

convertidor_binario()