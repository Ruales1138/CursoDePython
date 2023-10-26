value = input("Ingresa tres valores separados por comas: ")

nums = value.split(',')
num1 = int(nums[0])
num2 = int(nums[1])
num3 = int(nums[2])

maxNum = max(num1, num2, num3)
minNum = min(num1, num2, num3)

print("Numero maximo: {}".format(maxNum))
print("Numero minimo:", minNum)