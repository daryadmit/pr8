size = input("Введите размер квадрата (целое положительное число): ")

if size.isdigit():
  size = int(size)
  if size > 0:
    row = 0
    while row < size:
      col = 0
      while col < size:
        print("*", end="")
        col += 1
      print()
      row += 1
  else:
    print("Ошибка! Размер квадрата должен быть больше 0.")
else:
  print("Ошибка! Введите целое положительое число.")
