def calcular_promedio():
  
  suma_total = 0.0
  cantidad_numeros = 0

  print("Ingrese números uno por uno para calcular su promedio.")
  print("Ingrese un número negativo para finalizar y ver el resultado.")

  
  while True:
    try:
      
      entrada = input(f"Ingrese un número (llevas {cantidad_numeros} números): ")
      numero = float(entrada) 

      
      if numero < 0:
        print("--- Ha ingresado un número negativo. Calculando el promedio... ---")
        break 

      suma_total += numero
      cantidad_numeros += 1  

    except ValueError:
      
      print("Error: Por favor, ingrese un valor numérico válido.")

  if cantidad_numeros > 0:
   
    promedio = suma_total / cantidad_numeros

    print("\n------ Resultado Final ------")
    print(f"Cantidad de números ingresados: {cantidad_numeros}")
    print(f"Suma total de los números: {suma_total}")
    
    print(f"✅ El promedio de los números es: {promedio:.2f}")
  else:
   
    print("\n❌ No se ingresaron números válidos, no se puede calcular el promedio.")

calcular_promedio()