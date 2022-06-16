import random

print("bienvenido adivina el numero!")
print("Las reglas son simples. Pensare en un numero, e intentaras adinarlo.")

number = random.randint(1,10)

isGuessRight = False

while isGuessRight != True:
    guess = input("Adivine un numero entre 1 y 10 ")
    if int(guess) == number:
        print("Adivinaste {}. Es corecto Adivinaste".format(guess))
        isGuessRight = True
    else:
        print("No adivinaste {}. lo siento, Respuesta incorrrecta. Intenta de nuevo.".format(guess))
        

for x in range (0, 11):
    print(x)