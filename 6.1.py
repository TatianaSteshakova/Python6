n = int(input("Введите n: "))

cnt = 0

print("Введите n чисел: ")
for i in range (0, n):
    num = int(input())
    if (num == 0):
        cnt += 1

print("Количество нулей:", cnt)
