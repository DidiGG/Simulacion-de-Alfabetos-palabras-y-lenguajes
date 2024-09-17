"""Verifica si la palabra esta utilizando el metodo de cerradura positiva"""
def verificarPertenenciaLenguaje(alfabeto,palabra,lenguaje):
    iteraciones=len(palabra)
    while iteraciones>0:
        j=0
        limiteApoyo = len(lenguaje) #Despues de concaternar el alfabeto con una de sus combinaciones, aumenta la cantidad de de pisicones
        #del lenguaje a las que puede acceder el codigo. Hay que tener en cuenta que, como la variable lenguaje se le agregan mas elementos en plena concatenacion con la
        #variable alfabeto, no se puede permitir que el codigo acceda a las posiciones nuevas que se supone que hacen parte de la combinacion resultante y no
        #de la combinacion con la que se esta concatenando el alfabeto
        while j<len(alfabeto)-1:
            k=0
            while k<limiteApoyo:
                lenguaje.append(alfabeto[j]+lenguaje[k])
                k+=1
            j+=1
        iteraciones -= 1
    lenguajeConjunto=set() #Se inicializa un conjunto para eliminar posibles elementos repetidos
    lenguajeConjunto.update(lenguaje) #Al conjunto se le agregan los elementos de la variable lenguaje
    print(lenguajeConjunto)
    print(len(lenguajeConjunto))
    if palabra in lenguajeConjunto:
        return True
    return False

"""A la variable lenguaje se le agregan los elementos de la variable alfabeto"""
def igualarArreglo(alfabeto):
    i=0
    lenguaje=[]
    while i<len(alfabeto):
        lenguaje.append(alfabeto[i])
        i+=1
    return lenguaje




alfabeto=['a','bx','ca','dor']
palabra='caador'
lenguaje=igualarArreglo(alfabeto)
estaONo=verificarPertenenciaLenguaje(alfabeto,palabra,lenguaje)
print(estaONo)