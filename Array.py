import random

array=[]

for i in range(10):
    num=random.randint(0,100)
    array.append(num)

print("Los elementos del arreglo son:")
for i in range(10):
    print(f"Posición {i+1} :  {array[i]}")

print("\nEn orden inverso: ")
for i in range(9,-1,-1):
    print(array[i], end=" ")


