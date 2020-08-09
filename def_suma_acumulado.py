"""Si se pasa como argumento una lista vacía ([]), la función devolverá una lista vacía.
Imagina la siguiente lista [1, 2, 3, 4]. La función acumulado([1, 2, 3, 4]) devolverá [1, 3, 6, 10]. Como ves, cada elemento de la lista devuelta es [1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4]."""

def acumulado(string):
    suma = 0
    acumula = []
    try:
        for num in string:
            num = int(num)
            suma += num
            acumula.append(suma)
            
    except:
        
        if string == []:
            return(string)
        else:
            return("Error en formato de datos.")
    return acumula

res = acumulado([1, 5, 7])
print(res)
#[1, 6, 13]
res1 = acumulado([1, 0, 1, 0, 1])
print(res1)
#[1, 1, 2, 2, 3]
res2 = acumulado([])
print(res2)
#[]
