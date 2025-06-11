lista_numeros = [15, 23, 8, 42, 11, 19, 5, 31, 27, 4]
numero_encontrado = False

print(f"La lista es: {lista_numeros}")
try:
    numero_buscado = int(input("Ingrese el número que desea buscar en la lista: "))

    for i in range(len(lista_numeros)):
        
        if lista_numeros[i] == numero_buscado:
            print(f"\n ¡Éxito! El número {numero_buscado} se encuentra en la lista.")
            print(f"   Se encuentra en la posición (índice): {i}")
            numero_encontrado = True
            break 

    if not numero_encontrado:
        print(f"\n Lo sentimos, el número {numero_buscado} no se encuentra en la lista.")

except ValueError:
    print("\nError: Debe ingresar un número entero válido.")