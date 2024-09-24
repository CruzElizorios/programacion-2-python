# EJERCICIO 9
# Escriba una función recursiva que reciba un número positivo n y devuelva la cantidad 
# de dígitos que tiene

def contar_digitos(n):
    # Caso base: si n es menor que 10, solo tiene un dígito
    if n < 10:
        return 1
    # Llamada recursiva: divide n por 10 y suma 1 al resultado
    else:
        return 1 + contar_digitos(n // 10)

numero = 12489
print(f"contar_digitos({numero}) = ",contar_digitos(numero))

# EJERCICIO 9.1
# Escribe una función recursiva que calcule la suma de los dígitos de un número positivo.
# Dado un número 𝑛, la suma de sus dígitos es la suma del último dígito y la suma de los dígitos del resto del número.

def suma_digitos(n):
    if n == 0:
        return 0
    # n % 10 me quedo con la parte decimal ej 45%10=5 porque 45/10=4.5
    return n % 10 + suma_digitos(n//10)

print(f"suma_digitos({numero}) = ",suma_digitos(numero))
