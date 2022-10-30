# primeros ejemplos
x = 5
print(id(x)) # un objeto

x = 5
print(id(x)) # es el mismo objeto

x = 6
print(id(x)) # otro objeto (Ha cambiado)

x = 5
print(id(x)) # es otro objeto (Ha cambiado)

x = x + 1
print(id(x)) # otro objeto (Ha cambiado)
