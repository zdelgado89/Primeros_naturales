# entrada
N = int(input("hasta que numero natural quiere sumar?:"))

# proceso 
suma = 0 
X = 1
while(X<=N):
    suma = suma + X
    X = X + 1

# salida
print("la suma de los numeros naturales hasta", str(N), "es igual a", suma)
 