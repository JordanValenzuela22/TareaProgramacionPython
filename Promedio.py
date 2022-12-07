n=int(input("Ingrese la cantidad de datos: "))
acum=0
for i in range(n):
    dato=int(input(f"Ingrese el dato {i} : "))
    acum=acum+dato

prom=acum/n
print("El promedio es: ",prom)