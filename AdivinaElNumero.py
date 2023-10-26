import random

winningNumber = random.randint(1, 10)
answer = int(input("Adivina un numero entre 1 a 10: "))

if answer == winningNumber:
    print("¡Adivinaste!")

if answer != winningNumber:
    print("Perdiste")

print("El numero ganador era {}".format(winningNumber))