
def ingresar_matriz():
    matriz = []
    print("Ingresa los valores de la matriz (3x3):")
    for i in range(3):
        fila = []
        for j in range(3):
            valor = int(input(f"Ingresa el valor para la posición ({i+1},{j+1}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def mostrar_matriz(matriz):
    print("Matriz:")
    for fila in matriz:
        print("\t".join(map(str, fila)))

def suma_total(matriz):
    return sum(sum(fila) for fila in matriz)

def suma_filas_columnas(matriz):
    print("\nSuma de las filas:")
    for i, fila in enumerate(matriz):
        print(f"Suma de la fila {i+1}: {sum(fila)}")
    
    print("\nSuma de las columnas:")
    for j in range(3):
        suma_columna = sum(matriz[i][j] for i in range(3))
        print(f"Suma de la columna {j+1}: {suma_columna}")

def maximo_minimo(matriz):
    maximo = max(max(fila) for fila in matriz)
    minimo = min(min(fila) for fila in matriz)
    return maximo, minimo

def main():
    matriz = ingresar_matriz()
    
    mostrar_matriz(matriz)
    
    print(f"\nSuma total de los elementos de la matriz: {suma_total(matriz)}")
    
    suma_filas_columnas(matriz)
    
    maximo, minimo = maximo_minimo(matriz)
    print(f"\nNúmero mayor de la matriz: {maximo}")
    print(f"Número menor de la matriz: {minimo}")

main()

