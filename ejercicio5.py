
matriz = []
positivos = 0
negativos = 0
ceros = 0
suma_diagonal_principal = 0
suma_diagonal_secundaria = 0


print("Ingrese los elementos de la matriz de 3x3:")
for i in range(3):
    
    fila = []
    for j in range(3):
        
        numero = int(input(f"Ingrese el elemento para la posición [{i}][{j}]: "))
        fila.append(numero)
    matriz.append(fila)

for i in range(3):
    for j in range(3):
        elemento = matriz[i][j]
        if elemento > 0:
            positivos += 1
        elif elemento < 0:
            negativos += 1
        else:
            ceros += 1
        if i == j:
            suma_diagonal_principal += elemento
