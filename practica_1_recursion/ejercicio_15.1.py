# EJERCICIO EXTRA RECURSIVIDAD CON STRINGS
# Escribe una función recursiva que invierta una cadena de texto.

def invertir_cadena(texto: str) -> str:
    # cuando la cadena solo tenga un elemento, termino la función y retorno esa letra
    if len(texto) == 1:
        #print(texto)
        return texto
    #print(texto)
    # tomo el último valor de la cadena, vuelvo a llamar a la función pero texto ahora no incluye la última letra
    return texto[-1] + invertir_cadena(texto[:(len(texto)-1)])
    #return invertir_cadena(texto[1:]) + texto[0] # hace lo mismo

print("invertida: ",invertir_cadena("hola"))
# invertir_cadena(hola) -> a + loh => aloh
# invertir_cadena(hol) -> l + oh
# invertir_cadena(ho) -> o + h
# invertir_cadena(h) -> h
print("invertida: ",invertir_cadena("casa pato"))
print("invertida: ",invertir_cadena("otap asac"))
