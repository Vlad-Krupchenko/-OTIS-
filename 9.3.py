month = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
A = {}

for i in month:
    trans = input("Переклад для " + i + ": ")
    A[i] = trans

for i in A:
    print(i, A[i])