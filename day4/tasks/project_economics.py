"""
ЗАДАНИЕ 3: Расширенный анализ стран
Дан список стран с показателями за 3 года:
"""
"""
Для каждой страны:
1. Посчитай средний ВВП за 3 года
2. Посчитай среднюю инфляцию за 3 года
3. Определи, росла экономика в целом или падала
   (сравни первый и последний год)
4. Выведи итоговый отчет
"""

countries_data = [
    {
        "name": "Россия",
        "gdp": [2.1, 2.3, 1.8],  # ВВП за 2022, 2023, 2024
        "inflation": [7.5, 6.8, 7.2]
    },
    {
        "name": "США",
        "gdp": [2.5, 2.1, 2.8],
        "inflation": [3.2, 3.5, 2.9]
    },
    {
        "name": "Китай",
        "gdp": [5.2, 4.9, 5.5],
        "inflation": [2.1, 2.3, 1.9]
    }
]
print("\n--- ЗАДАНИЕ 3: Многолетний анализ ---")
summer_countries = []
for country in countries_data:
    summer = {
        "name": country["name"],
        "gdp_avg": sum(country["gdp"]) / len(country["gdp"]),
        "inflation_avg": sum(country["inflation"]) / len(country["inflation"]), 
        "growing": "Рост" if country["gdp"][-1] > country["gdp"][0] else "Падение",
        "health":  (country["gdp"][-1] * 2) - (country["inflation"][-1])
    }
    summer_countries.append(summer)

print(f"{"Страна":10}|{"Средний ВВП":11}|{"Средняя инфляция":15}|{"Рост за последний год":12}")
for country in summer_countries:
    print(f"{country["name"]:10}|{country["gdp_avg"]:11,.2f}|{country["inflation_avg"]:16.2f}|{country["growing"]:12}")

"""
ЗАДАНИЕ 4: Рейтинг стран
Используя данные из задания 3:
1. Найди страну с максимальным средним ВВП
2. Найди страну с минимальной инфляцией
3. Выведи топ-стран по "здоровью экономики"
   (ВВП - инфляция/2)
"""

print("\n--- ЗАДАНИЕ 4: Рейтингование ---")
max_avg_gdp = max(summer_countries, key=lambda country: country["gdp_avg"])
min_avg_inflation = min(summer_countries, key=lambda country: country["inflation_avg"])
sorted_by_health = sorted(summer_countries, key=lambda country: country["health"], reverse=True)

print(f"Страна с максимальным средним ростом ВВП: {max_avg_gdp["name"]}")
print(f"Страна с максимальным средней инфляцией: {min_avg_inflation["name"]}")
print("Топ-стран по здоровью экономики:")
for country in sorted_by_health:
    print(f"{country['name']}: {country["health"]:.2f}")
