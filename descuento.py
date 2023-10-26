age = int(input("Dime tu edad: "))
typeOfCard = input("Dime tu tipo de carnet (E: Estudiante / P: Pensionista / F: Familia numerosa / N: Nada): ")

if ((25 <= age <= 35 and typeOfCard == "E") or
        age <= 10 or
        (age >= 65 and typeOfCard == "P") or
        typeOfCard == "F"):
    print("Se te aplica el descuento")
else:
    print("No se te aplica en descuento")