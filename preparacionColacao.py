print("Me voy a la cosina")
print("Abro la nevera")

hay_leche = input("Hay leche? (S/N): ")
hay_colacao = input("Hay colacao? (S/N): ")

if hay_leche != "S" or hay_colacao != "S":
    print("Voy hasta el super")
    if hay_leche != "S":
        print("Compro leche")
    if hay_colacao != "S":
        print("Compro colacao")

print("Ponemos la leche en el vaso")
print("Ponemos el colacao en el vaso")
print("Mesclamos")