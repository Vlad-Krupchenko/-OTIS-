n = int(input("Кількість слів: "))
words = []
for i in range(n):
    words.append(input("? "))

start_char = {}

for i in words:
    if i[0] not in start_char:
        start_char[i[0]] = 0
    start_char[i[0]] += 1

print(start_char)