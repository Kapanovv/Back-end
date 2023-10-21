print("Добро пожаловать вы заполняете анкету")
name=input("Введите ваше имя:")
surname=input("Введите вашу фамилию:")
year=input("Введите ваш год рождение:")
review_1=input("Нравиться ли вам курс?")
review_2=input("Что вы ожидаете в дальнейших занятиях?")
full_age= f"Вам {2023-int(year)} лет"
full_name=name + " " + surname

print("Вы заполнили такие данные:")

print("Вас зовут:", full_name)
print(full_age)
print("Ваш ответ к первому вопросу:",review_1)
print("Ваш ответ к второму вопросу:",review_2)