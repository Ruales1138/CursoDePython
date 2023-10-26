value = float(input("Ingresa grados fahrenheit: "))
result = (value - 32) * 5 / 9

value2 = float(input("Ingrese valor en dolares: "))
result2 = value2 * 4260.27

print("Conversion a grados celsius:", result)
print("Conversion a pesos colombianos: ${}".format(result2))