def contar_vocales_y_consonantes():
  
  vocales = "aeiou"

  contador_vocales = 0
  contador_consonantes = 0

  cadena_texto = input("Por favor, ingrese una cadena de texto: ")

  for caracter in cadena_texto:

    caracter_lower = caracter.lower()

    if caracter_lower.isalpha():
    
      if caracter_lower in vocales:
        contador_vocales += 1
      else:
        
        contador_consonantes += 1

  print("\n--- Resultados del Análisis ---")
  print(f"Texto analizado: '{cadena_texto}'")
  print(f"Número de vocales: {contador_vocales}")
  print(f"Número de consonantes: {contador_consonantes}")
