print("\n" + "="*60)
print("БОНУС: БЕСКОНЕЧНЫЙ ВВОД (while)")
print("="*60)

"""
ЗАДАНИЕ 5: Таможенный терминал
Создай программу, которая:
1. В цикле (while True) принимает товары
2. После каждого товара спрашивает: "Добавить еще? (да/нет)"
3. Если "нет" - выходит из цикла и показывает итоги
4. Если "да" - продолжает ввод
"""

print("\n--- ЗАДАНИЕ 5: Интерактивный ввод ---")
choices = ["да", "нет"]
products = []

print("Введите товары для оформления:")
while True:
    name = input("Наименование товара: ")
    price_usd = float(input("Стоимость товара в USD: "))
    weight_kg = float(input("Вес товара в кг: "))
    product = {
            "name": name,
            "price_usd": price_usd,
            "weight_kg": weight_kg
    }
    products.append(product)
    choice = ""    
    while True:
        choice = input("Добавить еще? (да/нет): ")
        if choice not in choices:
            print("Нужно ввести (да/нет)")
            continue
        else:
            break
    if choice == "нет":
        break


print("\n✅ Список товаров готов!")
for index, product in enumerate(products, 1):
    print(f"\tТовар №{index}")
    print(f"Описание: {product["name"]}")
    print(f"Стоимость в USD: {product["price_usd"]}")
    print(f"Вес в кг: {product["weight_kg"]}")
