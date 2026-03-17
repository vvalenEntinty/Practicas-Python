import random

guessed = []
attempts = 6
point = 0
categorias = {
    "tipo de dato" : ["entero", "cadena", "lista"],
    "estructura de control" : ["bucle", "funcion"],
    "lenguaje de programacion" : ["python", "programa"]
}

print("¡Bienvenido al Ahorcado!")
print()
print("Categorías disponibles:")
for category in categorias:
    print(f"- {category}")
print()

selected_category = input("Seleccioná una categoría: ")
while selected_category not in categorias:
    print("Categoría no válida. Por favor, seleccioná una categoría de la lista.")
    selected_category = input("Seleccioná una categoría: ")
word = random.choice(categorias[selected_category])
while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        point +=6
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ")

    if (len(letter) != 1 ) or (not letter.isalpha()):
        print("Por favor, ingresá una letra válida.")
        continue
 
    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        point -= 1
        print("Esa letra no está en la palabra.")
    print()
else:
    print(f"¡Perdiste! La palabra era: {word}")
    point=0
print (f"Tu puntaje es: {point}")