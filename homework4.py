a = input("Введите первое число (целое): ")
b = input("Введите второе число (целое): ")

def is_integer(s):
    if s.startswith('-'):
        return s[1:].isdigit()
    return s.isdigit()

if is_integer(a) and is_integer(b):
    a = int(a)
    b = int(b)

    if a > b:
        a, b = b, a

    for i in range(a + 1, b):
        print(i)
else:
    print("Введите целые числа.")