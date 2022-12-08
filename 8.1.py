import array
import random

arr = array.array("i", [])

a = int(input("a="))
b = int(input("b="))

for i in range(10):
    arr.append(random.randint(a, b))

elem = []

print(arr)

i = 0
while i < len(arr):
    if arr[i] in elem:
        del arr[i]
    else:
        elem.append(arr[i])
        i += 1

print(arr)
