import random

numero_secreto = random.randint(1, 99)
cant_intentos = 0
cant_max_intentos = 10
adivinado = False

print("¡Bienvenido al juego de adivinar el número secreto!")
print("Tienes 10 intentos!")

while not adivinado and cant_intentos < cant_max_intentos:
    entrada = input("Introduce un número del 1 al 99: ")
    
    # Verificación de que la entrada es un número válido
    try:
        numero = int(entrada)
    except ValueError:
        print("Por favor, introduce un número válido.")
        continue
    
    # Verificación del rango
    if numero < 1 or numero > 99:
        print("El número debe estar entre 1 y 99. Inténtalo de nuevo.")
        continue
    
    # Verificación del número secreto
    if numero == numero_secreto:
        print("¡Felicitaciones, has adivinado el número secreto!")
        adivinado = True
    elif numero < numero_secreto:
        print("El número es mayor al número ingresado.")
    else:
        print("El número es menor al ingresado.")
    
    cant_intentos += 1

if not adivinado:
    print("Game Over. El número secreto era:", numero_secreto)
