print("="*60)
print("ЗАЧЕМ НУЖНЫ ФУНКЦИИ?")
print("="*60)

# ПЛОХОЙ ПОДХОД (без функций)
print("\n❌ БЕЗ ФУНКЦИЙ - код повторяется:")

# Считаем пошлину для первого товара
price1 = 1000
duty1 = price1 * 0.15
print(f"Товар 1: пошлина {duty1}")

# Считаем пошлину для второго товара (копипаст!)
price2 = 2000
duty2 = price2 * 0.15
print(f"Товар 2: пошлина {duty2}")

# Считаем пошлину для третьего товара (опять копипаст!)
price3 = 1500
duty3 = price3 * 0.15
print(f"Товар 3: пошлина {duty3}")

# ХОРОШИЙ ПОДХОД (с функцией)
print(f"\n✅ С ФУНКЦИЯМИ - код переиспользуется:")

def calculate_duty(price, rate = 0.15):
    """Рассчитывает таможенную пошлину"""
    return price * rate

# Одна строка вместо трех повторяющихся блоков
print(f"Товар 1: пошлина {calculate_duty(1000)}")
print(f"Товар 2: пошлина {calculate_duty(2000)}")
print(f"Товар 3: пошлина {calculate_duty(1500)}")

print("\n" + "="*60)
print("СИНТАКСИС ФУНКЦИЙ")
print("="*60)

# Базовая функция без параметров
def greet():
    """Докстринг - описание функции"""
    print("Привет, мир!")

greet()  # вызов функции

# Функция с параметрами
def greet_person(name):
    print(f"Привет, {name}!")

greet_person("Алексей") 

# Функция с возвратом значения
def add(a, b):
    result = a + b
    return result

summa = add(5, 3)
print(f"5 + 3 = {summa}")

print("\n" + "="*60)
print("ПАРАМЕТРЫ И АРГУМЕНТЫ")
print("="*60)

# Обязательные параметры
def create_product(name, price, weight):
    return {
        "name": name,
        "price": price,
        "weight": weight
    }
# Параметры по умолчанию
def create_product_with_defaults(name, price, weight = 1.0, currency = "USD"):
    return {
        "name": name,
        "price": price,
        "weight": weight,
        "currency": currency
    }
# Можно не указывать weight и currency
p1 = create_product_with_defaults("Телефон", 500)
# Можно указать только weight
p2 = create_product_with_defaults("Ноутбук", 1000, 2.5)
# Можно указать все
p3 = create_product_with_defaults("Сервер", 5000, 15.0, "EUR")

print(p1)
print(p2)
print(p3)


print("\n" + "="*60)
print("ИМЕНОВАННЫЕ АРГУМЕНТЫ")
print("="*60)

def describe_country(name, population, gdp, capital = None):
    description = f"Страна: {name}, Население: {population} млн, ВВП: {gdp} трлн $"
    if capital:
        description += f", Столица: {capital}"
    return description
# Можно передавать в любом порядке, если указать имена
print(describe_country(
    name="Россия", 
    gdp=2.1, 
    population=146, 
    capital="Москва"
))
print(describe_country(
    population=38, 
    name="Канада", 
    gdp=2.2
))

print("\n" + "="*60)
print("*args И **kwargs - ГИБКИЕ ПАРАМЕТРЫ")
print("="*60)

# *args - любое количество позиционных аргументов
def sum_all(*args):
     """Суммирует любое количество чисел"""
     total = 0
     for num in args:
         total += num
     return total

print(f"Сумма 1,2,3: {sum_all(1,2,3)}")
print(f"Сумма 10,20,30,40,50: {sum_all(10,20,30,40,50)}")

# **kwargs - любое количество именованных аргументов
def print_product_info(**kwargs):
     """Выводит информацию о товаре из любых параметров"""
     print("Информация о товаре:")
     for key, value in kwargs.items():
         print(f"  {key}: {value}")

print_product_info(
    name="Ноутбук", 
    price=1000, 
    brand="Lenovo", 
    color="Silver"
)

print("\n" + "="*60)
print("ОБЛАСТИ ВИДИМОСТИ (SCOPE)")
print("="*60)

# Глобальная переменная
global_var = "Я глобальная"

def test_scope():
    """Локальная переменная"""
    local_var = "Я локальная"
    print(f"Внутри функции: {local_var}")
    print(f"Внутри функции вижу глобальную: {global_var}")

test_scope()
# print(local_var)  # Ошибка! local_var не видна снаружи

counter = 0
def increment():
    global counter  # говорим Python, что хотим менять глобальную
    counter += 1
    print(f"counter внутри функции: {counter}")

increment()
increment()
print(f"counter после вызовов: {counter}")