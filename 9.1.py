import random
j = ("січень", "лютий", "березень", "квітень", "травень", "червень", "липень", "серпень","вересень", "жовтень", "листопад", "грудень")
k = (2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030)
n=int(input("Введіть число"))
for i in range(n):
    print(random.randint(1,31),random.choice(j),random.choice(k))
    

