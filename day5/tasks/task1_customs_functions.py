"""
ЗАДАНИЕ 1: Таможенные функции
Перепиши код из предыдущих дней с использованием функций
"""
"""Программа для расчета таможенных платежей с логикой"""

print("="*50)
print("ТАМОЖЕННЫЙ КАЛЬКУЛЯТОР (ПРОДВИНУТЫЙ)")
print("="*50)

def create_product(name, price_usd, weight_kg, country_departure):
    """Функция создания товара"""
    return {
        "name": name,
        "price_usd": price_usd,
        "weight_kg": weight_kg,
        "country_departure": country_departure        
    }
def get_duty_rate(price_rub, country_departure):
    """Функция определения ставки пошлины"""
    
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
    
    return duty_rate




