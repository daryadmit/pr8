total = 0

while True:
    user_input = input("Введите число ('stop' или 'end' для завершения): ")

    if user_input.lower() == 'stop' or user_input.lower() == 'end':
        break

    if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
        total += int(user_input)
    else:
        print("Неправильный ввод. Пожалуйста, введите целое число.")

print("Сумма введенных чисел:", total)
