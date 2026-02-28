print("="*50)
print("ЦИКЛ for - ОСНОВЫ")
print("="*50)

#Самый простой цикл - перебор списка
fruits = ["яблоко", "банан", "апельсин"]
for fruit in fruits:
    print(f"Фрукт: {fruit}")

# range(5) создает числа от 0 до 4
print("\nЧисла от 0 до 4:")
for i in range(5):
    print(f"Число: {i}")

# range(1, 10, 2) от 1 до 9 с шагом 2
print("\nНечетные числа от 1 до 9:")
for i in range(1, 10, 2):
    print(f"Число: {i}")

# Часто используется для повторения действия N раз
print(f"\nДелаем что-то 3 раза:")
for i in range(3):
    print(f"Действие {i+1}: Отправляем запрос к API...")

print("\nПЕРЕБОР С ИНДЕКСАМИ:")
countries = ["Россия", "США", "Китай"]
for index, country in enumerate(countries, 1):
    print(f"{index}. {country}")

print("\nПЕРЕБОР СЛОВАРЕЙ:")
# Словарь с данными страны
country = {
    "name": "Россия",
    "gdp": 2.1,
    "inflation": 7.5,
    "capital": "Москва"
}
# Перебор ключей
print("\nКлючи:")
for key in country.keys():
    print(f"   {key}")

# Перебор значений
print("\nЗначения:")
for value in country.values():
    print(f"   {value}")

# Перебор пар ключ-значение
print("\nПары ключ-значение:")
for key, value in country.items():
    print(f"  {key}: {value}")

print("\n" + "="*50)
print("ЦИКЛ while - ОСНОВЫ")
print("="*50)

#Счетчик
counter = 1

while counter <= 5:
    print(f"Итерация {counter}")
    counter += 1  # Важно! Не забывать увеличивать счетчик   

print("\nВВОД ДАННЫХ ДО КОРРЕКТНОГО ЗНАЧЕНИЯ:")
#Запрашиваем возраст, пока не введут число >= 0
age = -1
while age < 0:
    try:
        age = int(input("Введите ваш возраст: "))
        if age < 0:
            print("Возраст не может быть отрицательным!")
    except ValueError:
        print("Пожалуйста, введите число!")

print(f"Ваш возраст: {age}")

print("\n" + "="*50)
print("BREAK - ПРЕРЫВАНИЕ ЦИКЛА")
print("="*50)

#Ищем первый отрицательный элемент
numbers = [5, 3, 8, -2, 10, 7, -1, 4]

for num in numbers:
    if num < 0:
        print(f"Нашли отрицательное число: {num}.  Останавливаемся.")
        break
    print(f"Обрабатываем {num}")

print("\n" + "="*50)
print("CONTINUE - ПРОПУСК ИТЕРАЦИИ")
print("="*50)

#Обрабатываем только положительные числа
for num in numbers:
    if num <= 0:
        print(f"Пропускаем {num} (не положительное)")
        continue
    print(f"Обрабатываем положительное число: {num}")

print("\n" + "="*50)
print("ВЛОЖЕННЫЕ ЦИКЛЫ")
print("="*50)

#Таблица умножения 3x3
for i in range(1, 4):
    for j in range(1, 4):
         print(f"{i} * {j} = {i*j}", end="\t")
    print() # Переход на новую строку