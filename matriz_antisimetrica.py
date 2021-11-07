# Define una rutina que devuelve True si una matriz es
# atisimetrica y False en otro caso. 
# Una matriz n*n es antisimetrica si se verifica que 
# sus elementos mantienen la relación:
# matriz[i][j] = - matriz[j][i] 
# para cada i=0,1,...,n-1 y para cada j=0,1,...,n-1.

def esMatrizCuadrada(matriz):

    # chequeamos que sea una lista
    if not isinstance(matriz, list):
        return 'El input debe ser una lista'

    # chequeamos que sea cuadrada
    for fila in matriz:
        if len(fila) != len(matriz):
            return False
        
    return True


def esAntisimetrica(matriz):
    
    if esMatrizCuadrada(matriz):
        
        for indiceFila in range(len(matriz)):
            for indiceColumna in range(len(matriz)):
                if matriz[indiceFila][indiceColumna] != -matriz[indiceColumna][indiceFila]:
                    return False
        return True
    
    else:
        return False



# Casos Test:

print(esAntisimetrica([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]]))   
#>>> True

print(esAntisimetrica([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]))
#>>> True

print(esAntisimetrica([[0, 1, 2], 
                     [-1, 0, -2], 
                     [2, 2,  3]]))
#>>> False

print (esAntisimetrica([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]]))
#>>> False

# casos test que no satisfacen la precondicion de que la matriz sea cuadrada (assert)

matriz4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

print(esAntisimetrica(matriz4))
#>>>False

matriz5 = [[1,0,0,0,0,0,0,0,0]]

print(esAntisimetrica(matriz5))
#>>>False 