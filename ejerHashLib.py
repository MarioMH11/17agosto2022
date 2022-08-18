import hashlib
from hmac import digest

class Hash:
    def generarHash():
        digest=h.hexdigest()
        return digest

x=0

while x<1:
    print("Elija el algoritmo que desea utilizar")
    print("\n1. Sha256 \n2.Sha512 \n3. Salir ")
    opcion=int ((input("Opcion seleccionada: ")))
    
    algoritmo=""

    if opcion!=3:
        if opcion==1:
            datos=input("Introduzca los datos para hash:")
            algoritmo="sha256"
        elif opcion==2:
            datos=input("Introduzca los datos para hash:")
            algoritmo="sha512"

        texto=bytes(datos, 'utf-8')
        h=hashlib.new(algoritmo,texto)
        hash1= Hash.generarHash(h)
        print(hash1)
        x=0