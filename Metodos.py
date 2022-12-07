def Saludar():
    print("Hola mundo!")

def CalcularDoble(num):
    return num*2

def Triplicar(num):
    return num*3

print("Llamada a la funcion Saludar:")
Saludar()

x=int(input("Ingrese un valor numérico para x: "))

print("Llamada a la función CalcularDoble (pasaje por valor)")
print("El doble de ",x," es ", CalcularDoble(x))
print("El valor original de x es ",x)
print("Llamada a la función Triplicar (pasaje por referencia)")
Triplicar(x)
x=Triplicar(x)
print("El nuevo valor de x es ", x)
