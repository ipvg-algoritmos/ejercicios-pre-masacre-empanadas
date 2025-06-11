def encontrar_mayor_y_menor():
  
  numeros_ingresados = []

  print("Ingrese números uno por uno. Ingrese un número negativo para finalizar.")

  
  while True:
    try:
      
      entrada = input(f"Ingrese un número (actuales: {len(numeros_ingresados)}): ")
      numero = float(entrada) 

      if numero < 0:
        print("--- Ha ingresado un número negativo. Finalizando la entrada de datos. ---")
        break 

      numeros_ingresados.append(numero)

    except ValueError:
      
      print("Error: Por favor, ingrese un valor numérico válido.")

  if len(numeros_ingresados) > 0:

    numero_mayor = max(numeros_ingresados)
    numero_menor = min(numeros_ingresados)

    print("\nAnálisis de la lista completado:")
    print(f"La lista de números ingresados es: {numeros_ingresados}")
    print(f" El número mayor de la lista es: {numero_mayor}")
    print(f" El número menor de la lista es: {numero_menor}")
  else:
    
    print("\n No se ingresaron números válidos para analizar.")

encontrar_mayor_y_menor()