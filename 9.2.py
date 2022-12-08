import random
A = set()

for i in range(100):
    A.add(random.randint(1, 500))

B_v = input("Введіть B через пробіл: ").split(" ")
B = set(B_v)

print("1) ")
for i in B:
    if i in A:
        print(i)

print("2) ")
for i in A:
    if i not in B:
        print(i)

print("3) ")
for i in B:
    if i not in A:
        print(i)
