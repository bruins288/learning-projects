#Задание 1 (Проект 2 - таможня):
#Напиши программу, которая:
#1. Спрашивает у пользователя название товара.
#2. Спрашивает стоимость товара в долларах.
#3. Спрашивает курс доллара к рублю.
#4. Переводит стоимость в рубли.дрель
#5. Выводит итоговое сообщение: "Товар [название] стоит [сумма] рублей."

print("ПРОГРАММА КАЛЬКУЛЯТОР ТОВАРОВ")
print("\n"+"="*50)

product_name = input("Введите название товара: ")
product_cost_usd = float(input("Введите стоимость товара в USD: "))
exchange_rate = float(input("Введите курс USD/RUB: "))
product_cost_rub = product_cost_usd * exchange_rate
product_duty = product_cost_rub * (15/100)
product_vat = (product_cost_rub + product_duty)*(22/100)
print(f"Товар {product_name} стоит {product_cost_rub:.2f} рублей.")
print(f"Пошлина 15%: {product_duty:.2f} рублей.")
print(f"НДС 22%: {product_vat:.2f} рублей.")
