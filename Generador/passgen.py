import string
import random

longitud = int(input("Ingrese el numero de caracteres deseado: "))

caracateres = string.ascii_letters + string.digits + string.punctuation

contrasena = "".join(random.choice(caracateres) for i in range(longitud))

print("La contrasena generada es: " + contrasena)