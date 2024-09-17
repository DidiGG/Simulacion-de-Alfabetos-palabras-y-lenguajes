#Creamos un alfabeto de prueba
alfabeto = ['A', 'B', 'C']

#Lonfitud para el lenguaje 
longitud = 3

resultado = ['']

#Itera dentro de un rango determinado en la longitud de la palabra
for _  in range(longitud):
    nuevasPalabra = []

    #Recorre todas las palabras generadas hasta el momento    
    for palabra in resultado:
            #Toma cada letra del alfabeto y lo agrega al final de la palabra actual
            for letra in alfabeto:
                #Cada combinacion se añade a la lista
                nuevasPalabra.append(palabra + letra)

    resultado = nuevasPalabra

for palabra in resultado:
    print(palabra)

    



