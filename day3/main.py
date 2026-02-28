# Простейшее условие
age = 18

if age >= 18:
    print("Вы совершеннолетний")
else:
    print("Вы несовершеннолетний")

x = 10
y = 20

print(x == y)
print(x != y)
print(x < y)
print(x > y)

age = 25
has_license = True
has_car = False

#Может ли человек водить машину?
if age >= 18 and has_license:
    print("Может водить (есть права и возраст подходит)")
else:
    print("Не может водить")

#Может ли поехать на машине?
if has_car or (age >=18 and has_license):
    print("Может поехать на машине (либо своя есть, либо может арендовать)")

#Оценка ВВП
gdp_growth = float(input("Введите рост ВВП в %: "))

if gdp_growth > 5:
     print("Экономика растет очень быстро (бум)")
elif gdp_growth > 2:
    print("Экономика растет умеренно")
elif gdp_growth > 0:
    print("Экономика растет медленно")
elif gdp_growth == 0:
    print("Экономика стагнирует (не растет)")
else:
    print("Экономика падает (рецессия)")

#Тернарный оператор (одна строка)
status = "взрослый" if age >= 18 else "ребенок"