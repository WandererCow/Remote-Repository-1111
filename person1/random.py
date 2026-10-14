a = int(input())
b = int(input())
result = a + b

if a == 1:
    print(1)
elif a == 2:
    print(4)
elif a == 3:
    print(6)
elif a == 4:
    print(8)
elif a == 5:
    print(10)
elif a == 10:
    print(20)
else:
    print("Error: out of range")

a = True
while a is True:
    check = input("Правильно ли я посчитал?\n")
    a = False
    if check == "Да":
        print("Спасибо за обратную связь")
    elif check == "Нет":
        print("Вы совершенно правы, я не умею считать, прошу вас оставить подробный отзыв для улучшения моих вычислительных способностей!")
    else:
        a = True
