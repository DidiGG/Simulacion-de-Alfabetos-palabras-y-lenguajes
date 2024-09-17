""""Metodo recursivo que recibe el lenguaje, una variable auxiliar que permite recorrer
el lenguaje y la cadena que va a evaluar"""
def verificarPalabra(longitudArreglo,lenguaje,cadena):
    if longitudArreglo==len(lenguaje):
        return False
    else:
        if(lenguaje[longitudArreglo]==cadena):
            return True
        longitudArreglo+=1
        return verificarPalabra(longitudArreglo,lenguaje,cadena)


lenguaje=['Hola','ahola','lola']
verificarSiSeEncuentraPlabra=verificarPalabra(0,lenguaje,'ahola')
print(verificarSiSeEncuentraPlabra)