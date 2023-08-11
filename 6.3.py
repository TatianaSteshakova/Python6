a = int(input("Введите a: "))
b = int(input("Введите b: "))

txt = ""

if (a < b):
    for i in range(a, b+1):
        if (i % 2 == 0):
            txt = txt + str(i) + " "
    print(txt)
else:
    print("False")