# ¿QUE ES UN ANAGRAMA?


# Escribe una función que reciba dos palabras (String) y retorne
# verdadero o falso (Bool) según sean o no anagramas.
# - Un Anagrama consiste en formar una palabra reordenando TODAS
#   las letras de otra palabra inicial.
# - NO hace falta comprobar que ambas palabras existan.
# - Dos palabras exactamente iguales no son anagrama.

def anagrama(palabra_uno, palabra_dos):
    palabra_uno_ordenada = "".join(sorted(palabra_uno.upper()))
    palabra_dos_ordenada = "".join(sorted(palabra_dos.upper()))

    if palabra_uno_ordenada == palabra_dos_ordenada:
        print(True)
    else:
        print(False)


anagrama("Capi", "PiCa")
