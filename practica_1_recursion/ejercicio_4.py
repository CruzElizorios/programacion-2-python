def f(n: int, d: int) -> None:
    if n > 1:
        if n % d == 0:
            print(d)
            f(n // d, d)
        else:
            f(n, d + 1)
    
f(40,2)
# 4.3 función iterativa equivalente
def f_iterativo(n: int, d: int) -> None:
    if n > 1:
        if n % d == 0:
            pass
