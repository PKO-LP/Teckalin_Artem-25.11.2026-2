knigi = 0
print(f"Книг выдано: {knigi}")
while True:
    i = int(input(f"Введите команду: "))
    if i == 1:
      knigi += 1
      print(f"Книг выдано: {knigi}")
    elif i == 2:
       print(f"Книг выдано: {knigi}")
    elif i == 3:
       knigi = 0
       print(f"Книг выдано: {knigi}")
    elif i == 4:
        if knigi > 0:
          knigi -= 1
          print(f"Книг выдано: {knigi}")
        else:
          print("Нет выданных книг")
    elif i == 0:
       break
    else:
       print("ОШИБКА: команды не сущёствует")

    