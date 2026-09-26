"""/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */"""

def anagramas(palabra1, palabra2):

    sorted_palabra1 = sorted(palabra1.lower())
    sorted_palabra2 = sorted(palabra2.lower())

    if sorted_palabra1 == sorted_palabra2:
        return True
    else:
        return False


print(anagramas("Riesgo", "SERGIO"))