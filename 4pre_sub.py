def generar_palabras_con_prefijo_y_sufijo(alfabeto, longitud, prefijo, sufijo):
    # Verificar que prefijo y sufijo son válidos (pertenecen al alfabeto)
    if not all(letra in alfabeto for letra in prefijo):
        raise ValueError("El prefijo contiene letras que no están en el alfabeto.")
    if not all(letra in alfabeto for letra in sufijo):
        raise ValueError("El sufijo contiene letras que no están en el alfabeto.")
    
    # Verificar que la longitud permite incluir prefijo y sufijo
    if len(prefijo) + len(sufijo) > longitud:
        raise ValueError("La longitud total es menor que la suma del prefijo y sufijo.")

    # Generar el cuerpo de las palabras (sin el prefijo y sufijo)
    cuerpo_longitud = longitud - len(prefijo) - len(sufijo)
    resultado = [prefijo]

    for _ in range(cuerpo_longitud):
        nuevas_palabras = []
        for palabra in resultado:
            for letra in alfabeto:
                nuevas_palabras.append(palabra + letra)
        resultado = nuevas_palabras

    # Añadir el sufijo a todas las combinaciones generadas
    resultado = [palabra + sufijo for palabra in resultado]
    
    return resultado

alfabeto = ['A', 'B', 'C']
longitud = 5

# Generar palabras con prefijo "AB" y sufijo "C"
prefijo = "AB"
sufijo = "C"
palabras = generar_palabras_con_prefijo_y_sufijo(alfabeto, longitud, prefijo, sufijo)

print("Palabras con prefijo 'AB' y sufijo 'C':")
for palabra in palabras:
    print(palabra)
