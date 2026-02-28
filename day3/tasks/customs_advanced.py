"""Программа для расчета таможенных платежей с логикой"""

print("="*50)
print("ТАМОЖЕННЫЙ КАЛЬКУЛЯТОР (ПРОДВИНУТЫЙ)")
print("="*50)

#Ввод данных
product_name = input("Название товара: ")
country_departure = input("Страна отправления: ")
price_usd = float(input("Стоимость в USD: "))
exchange_rate = float(input("Курс USD/RUB: "))
weight_kg = float(input("Вес товара (кг): "))

#Переводим в рубли
price_rub = price_usd * exchange_rate

#Определяем ставку пошлины в зависимости от цены
if price_rub > 10_000:
    duty_rate = 20 #20% для дорогих товаров
    print("Применена повышенная ставка пошлины (товар дороже 10000 руб)")
elif price_rub > 5_000:
    duty_rate = 15 #15% для для средних
else:
    duty_rate = 10  # 10% для дешевых

#Страна отправления Китай    
if country_departure == "Китай":
    duty_rate -= 5 #льготный режим

#Проверка на превышение лимита беспошлинного ввоза
#(допустим, лимит 1000 евро = ~1000 * 100 руб = 100000 руб)
if price_rub > 100_000:
    print("ВНИМАНИЕ: Превышен лимит беспошлинного ввоза!")
    duty_rate += 30  #добавляем 30% штрафной пошлины

#Проверка на тяжеловесный груз

additional_fee = 0 # Вводим отдельную переменную для дополнительных сборов
if weight_kg > 50:
    print("Применен дополнительный сбор на тяжесть груза")
    additional_fee = 5_000  # Отдельный сбор

#Расчет пошлины
duty = price_rub * (duty_rate/100)

#НДС (стандартный 22% медикаменты 10%)
vat_rate = 22 if product_name != "медикаменты" else 10
vat = (price_rub + duty) * (vat_rate/100)

#Дополнительная проверка на подакцизные товары
excisable_goods = ["сигареты", "алкоголь", "бензин", "табак"]
if product_name.lower() in excisable_goods:
    print("Товар подакцизный!")
    excise_tax = price_rub * 0.10 # акциз 10%
    vat += excise_tax
    print(f"Добавлен акциз: {excise_tax:.2f} руб")

#Итоговый расчет
total_payment = price_rub + duty + vat + additional_fee

print("\n" + "-"*50)
print("РЕЗУЛЬТАТЫ РАСЧЕТА:")
print("-"*50)
print(f"Товар: {product_name}")
print(f"Вес: {weight_kg} кг")
print(f"Ставка пошлины: {duty_rate}%")
print(f"Стоимость товара: {price_rub:.2f} руб")
print(f"Пошлина: {duty:.2f} руб")
print(f"НДС + акцизы: {vat:.2f} руб")
print(f"ИТОГО к оплате: {total_payment:.2f} руб")
print("="*50)

# Рекомендация
if total_payment > price_rub * 1.5:
    print("⚠️  Совет: Проверьте, может быть дешевле заказать доставку из другой страны?")
elif total_payment < price_rub * 1.1:
    print("✅ Выгодная покупка! Платежи небольшие.")
else:
    print("📦 Обычная таможенная очистка.")