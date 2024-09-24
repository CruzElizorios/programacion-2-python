# La función potencia(b, n), que calcula la n-esima potencia de b, puede escribirse del siguiente modo, a
# partir de sus propiedades matemáticas
# -> b^0 = 1
# -> b^n= b^(n/2) * b^(n/2)           si n es par
# -> b^n= b^(n−1/2) * b^(n−1/2) * b   si n es impar

def potencia(b,n) -> float:
    if n == 0:
        return 1
    if n % 2 == 0:
        return potencia(b, n//2) * potencia(b, n//2)
    else:
        return potencia(b, (n-1)//2) * potencia(b, (n-1)//2) * b
    
print(potencia(2,3))
print(potencia(5,4))
print(potencia(4,2))

