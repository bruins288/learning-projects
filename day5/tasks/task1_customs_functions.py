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

def check_excess_penalty(price_rub, limit = 100_000, penalty = 30):
    """Функция проверки превышения лимита"""
    if price_rub > limit:
       print("ВНИМАНИЕ: Превышен лимит беспошлинного ввоза!")
       return penalty
    return 0

def get_heavy_fee(weight_kg, threshold = 50, fee= 5000):
    """Функция расчета сбора за тяжелый вес"""
    if weight_kg > threshold:
        print("Применен дополнительный сбор на тяжесть груза")
        return fee
    return 0

def get_excise_tax(price_rub, product_name, excise_rate = 10):
    """Функция расчета акциза"""
    if product_name.lower() in ["сигареты", "алкоголь", "бензин", "табак"]:
        print("Товар подакцизный!")
        return price_rub * (excise_rate / 100)
    return 0

def calculate_vat(product_name, price_rub, duty, vat_rate = 22):
    """Функция расчета НДС"""
    if product_name == "медикаменты":
        vat_rate = 10
    return (price_rub + duty) * (vat_rate/100)

def calculate_product_total(product, exchange_rate):
    """ Функция полного расчета одного товара"""
    price_rub = product["price_usd"] * exchange_rate
    duty_rate = get_duty_rate(price_rub, product["country_departure"])/100 + check_excess_penalty(price_rub)
    duty = price_rub * (duty_rate/100)
    vat =  calculate_vat(product["name"], price_rub, duty)
    excise = get_excise_tax(price_rub, product["name"])
    heavy_fee = get_heavy_fee(product["weight_kg"])

    return {
        "price_rub": price_rub,
        "duty_rate": duty_rate,
        "duty": duty,
        "vat": vat,
        "excise": excise,
        "heavy_fee": heavy_fee,
        "total": price_rub + duty + vat + excise + heavy_fee
    }
def print_product(product, calc_result = None):
    """Функция вывода информации о товаре"""
    print("\n" + "-"*50)
    print("РЕЗУЛЬТАТЫ РАСЧЕТА:")
    print("-"*50)
    print(f"Товар: {product["product_name"]}")
    print(f"Стоимость товара: {product["price_usd"]} usd")
    print(f"Вес: {product["weight_kg"]} кг")
    print(f"Страна отправления: {product["ountry_departure"]}")
    if calc_result:
        print(f"ИТОГО к оплате: {calc_result["total"]}")    
    print("="*50)

def process_products(products, exchange_rate):
    """Функция обработки списка товаров"""
    total_payment = {
        "total_price_rub": 0.0,
        "total_duty": 0.0,
        "total_vat": 0.0,
        "total_all": 0.0,
        "average_price": 0.0
    }
    for index, product in enumerate(products, 1):
        calc_product = calculate_product_total(product, exchange_rate)
        total_payment["total_price_rub"] += calc_product["price_rub"]
        total_payment["total_duty"] += calc_product["duty"]
        total_payment["total_vat"] += calc_product["vat"]
        total_payment["total_all"] += calc_product["total"]
        total_payment["average_price"] += calc_product["price_rub"] / index

    return total_payment

choices = ["да", "нет"]
products = []

print("Введите товары для оформления:")
while True:
    name = input("Наименование товара: ")
    price_usd = float(input("Стоимость товара в USD: "))
    weight_kg = float(input("Вес товара в кг: "))
    country_departure = input("Страна отправления: ")

    products.append(create_product(name, price_usd, weight_kg, country_departure))

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

for index, product in enumerate(products, 1):
    print(f"Товар №{index}")
    product_total = calculate_product_total(product, 77.2514)
    print_product(product, product_total)

products_total = process_products(products, 77.2514)
for key, value in products_total.items():
    print(f"{key}: {value}")
