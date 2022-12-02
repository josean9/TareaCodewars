def cube(n):
    arriba = '/\\'
    abajo = '\\/'
    lado1 = '_\\'
    lado2 = '_/'
    cubo = ""
    for row in range(n):     #Primero ponemos la parte de encima
        cubo += (n-row-1)* " " + (row+1)*arriba + n*lado1 + '\n'
    for row in reversed(range(n)):       #Con el reversed comenzamos a poner la parte de abajo
        cubo += (n-row-1)* " " + (row+1)*abajo + n*lado2 + '\n'
    return cubo[:-1]