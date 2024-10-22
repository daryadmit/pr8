while True:
    num1 = input("Введите первое целое положительное число: ")
    num2 = input("Введите второе целое положительное число: ")

    if num1.isdigit() and num2.isdigit():
        sum = int(num1) + int(num2)
        print("Сумма:", sum)
    else:
        print("Неверно! Введите целые положительные числа.")