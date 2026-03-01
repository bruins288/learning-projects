print("="*60)
print("ПРОЕКТ 2 (ТАМОЖНЯ): ПАКЕТНАЯ ОБРАБОТКА ТОВАРОВ")
print("="*60)

"""
ЗАДАНИЕ 1: Множественный ввод товаров
Напиши программу, которая:
1. Спрашивает у пользователя количество товаров
2. Для каждого товара запрашивает: название, цену в USD, вес
3. Сохраняет все товары в список
4. В конце выводит сводку по всем товарам
"""
print("\n--- ЗАДАНИЕ 1: Пакетные таможенные данные ---")
products_amount = int(input("Введите количество оформляемых товаров: "))
products = []

#Цикл опроса товаров и заполнения списка
if products_amount <= 0:
    print("⚠️ Количество товаров должно быть положительным!")
    exit()  # или products_amount = abs(products_amount)
if products_amount > 0: 
    for i in range(products_amount):
        print(f"Товар №{i+1}")
        name = input("Введите название товара: ")
        price_usd = float(input("Введите стоимость товара в USD: "))
        weight_kg = float(input("Введите вес товара в кг: "))
        product = {
            "name": name,
            "price_usd": price_usd,
            "weight_kg": weight_kg
        }
        products.append(product)        
    print("✅ Список товаров готов!\n")
    for index, product in enumerate(products, 1):
        print(f"\tТовар №{index}")
        print(f"Описание: {product["name"]}")
        print(f"Стоимость в USD: {product["price_usd"]}")
        print(f"Вес в кг: {product["weight_kg"]}")
else:
    print("⚠️ Нет оформляемых товаров!")   

print("\n" + "="*60)
print("ПРОЕКТ 2: РАСЧЕТ ИТОГОВ ПО ВСЕМ ТОВАРАМ")
print("="*60)
"""
ЗАДАНИЕ 2: Итоговый расчет
Используя список товаров из задания 1:
1. Посчитай общую стоимость всех товаров в USD
2. Посчитай общий вес
3. Посчитай среднюю цену товара
4. Найди самый дорогой товар
"""
print("\n--- ЗАДАНИЕ 2: Агрегация данных ---")
if products:
    total_price = 0
    total_weight = 0
    avg_price = 0
    max_price = 0
    max_prie_name = ""

    for product in products:
        total_price += product["price_usd"]
        total_weight += product["weight_kg"]
            
        if product["price_usd"] > max_price:
            max_price = product["price_usd"]
            max_prie_name = product["name"]

    print("Итоговые данные: ")
    print(f"Общая стоимость всех товаров: {total_price:.2f}")
    print(f"Общий вес всех товаров: {total_weight:.2f}")
    print(f"Средняя стоимость всех товаров: {total_price / products_amount:.2f}")
    print(f"Максимальная стоимость товара: {max_prie_name}: {max_price:.2f}")
