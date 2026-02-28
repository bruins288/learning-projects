"""
Программа для классификации экономических показателей стран
"""

print("="*50)
print("КЛАССИФИКАТОР ЭКОНОМИЧЕСКИХ ПОКАЗАТЕЛЕЙ")
print("="*50)

# Данные по странам (сами вводим или используем готовые)
countries = [
    {"name": "Россия", "gdp_growth": 2.1, "inflation": 7.5, "gdp_per_capita": 12000},
    {"name": "США", "gdp_growth": 2.5, "inflation": 3.2, "gdp_per_capita": 65000},
    {"name": "Китай", "gdp_growth": 5.2, "inflation": 2.1, "gdp_per_capita": 10500},
    {"name": "Германия", "gdp_growth": 0.8, "inflation": 2.8, "gdp_per_capita": 48000},
    {"name": "Зимбабве", "gdp_growth": -2.5, "inflation": 150, "gdp_per_capita": 1500}
]

countries_unfriendly = ["США", "Германия", "Франция", "Канада"]

print("\nАнализ стран:")
print("-"*50)

for country in countries:
    name = country["name"]
    growth = country["gdp_growth"]
    inflation = country["inflation"]
    gdp_per_capita = country["gdp_per_capita"]
    
    # Определяем статус экономики по росту ВВП
    if growth > 5:
        growth_status = "Бурный рост 🚀"
    elif growth > 2:
        growth_status = "Умеренный рост 📈"
    elif growth > 0:
        growth_status = "Слабый рост 📊"
    elif growth == 0:
        growth_status = "Стагнация ⏸️"
    else:
        growth_status = "Рецессия 📉"
    
    # Определяем уровень инфляции
    if inflation > 50:
        inflation_status = "Гиперинфляция 🔥"
    elif inflation > 10:
        inflation_status = "Высокая инфляция ⚠️"
    elif inflation > 5:
        inflation_status = "Повышенная инфляция 📈"
    elif inflation > 2:
        inflation_status = "Умеренная инфляция 📊"
    else:
        inflation_status = "Низкая инфляция ✅"
    
    # Определяем уровень развития по ВВП на душу
    if gdp_per_capita > 40000:
        development = "Развитая страна (высокий доход) 🌟"
    elif gdp_per_capita > 20000:
        development = "Страна с доходом выше среднего 💎"
    elif gdp_per_capita > 5000:
        development = "Развивающаяся страна 🌱"
    else:
        development = "Бедная страна 📌"
    
    #Рассчитать "индекс здоровья экономики"
    index_health = growth * 2 - inflation

    if index_health > 5:
        health_status = "Отлично"
    elif index_health > 0:
        health_status = "Нормально"
    else:
        health_status = "Плохо"
    
    # Выводим результат
    print(f"\n{name}:")
    print(f"  Рост ВВП: {growth}% - {growth_status}")
    print(f"  Инфляция: {inflation}% - {inflation_status}")
    print(f"  Уровень развития: {development}")
    print(f"  Индекс здоровья экономики: {health_status}")
    
    # Даем рекомендацию для инвесторов
    if growth > 3 and inflation < 5:
        print("  💰 ИНВЕСТИЦИОННЫЙ РЕЙТИНГ: Отличное место для инвестиций!")
    elif growth > 0 and inflation < 10:
        print(  "  💰 ИНВЕСТИЦИОННЫЙ РЕЙТИНГ: Можно рассматривать для вложений")
    elif growth < 0 or inflation > 20:
        print("  ⚠️  ИНВЕСТИЦИОННЫЙ РЕЙТИНГ: Высокий риск, осторожно!")
    else:
        print("  💰 ИНВЕСТИЦИОННЫЙ РЕЙТИНГ: Нейтральный")
    
    #Проверка на дружественность страны
    if name in countries_unfriendly:
        print("⚠️  Страна является недружественной, будьте осторожны!")