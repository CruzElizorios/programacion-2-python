# 11) Escriba una función recursiva que encuentre el mayor elemento de una lista.

lista_num=[1,5,10,7]

# def encontrar_mayor_recursivo( numeros:list[int] ) -> int:
#         mayor = numeros[0]
#         if len(numeros) == 1: 
#                 mayor = numeros [0]
#                 return mayor
#         elif numeros[0] > encontrar_mayor_recursivo(numeros.remove(numeros[0]) ): 
#             pass
                     

#         return encontrar_mayor_recursivo()

# def encontrar_mayor_iter( numeros:list[int]) -> int:
#     mayor = numeros[0]
#     for num in numeros:
#            if num > mayor:
#                 mayor = num
#     return mayor

# print(encontrar_mayor_iter(lista_num))
# lista_num.remove(lista_num[0])
# print(lista_num)

#Resolución profe

def mayor(lista: list) -> int:
    if len(lista) == 1: 
        return lista[0]
    
    primero = lista[0]
    resto = lista[1:]
    
    return max(primero,mayor(resto))

print("nueva resolución:", mayor(lista_num))
               
#------------
