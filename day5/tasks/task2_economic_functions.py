"""
ЗАДАНИЕ 2: Экономические функции
Создай функции для анализа экономических показателей
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

# TODO: Создай функцию average_gdp(gdp_list)
# которая считает средний ВВП за период
def average_gdp(gdp_list):
    """Считает средний ВВП за период"""
    return sum(gdp_list["gdp"])/len(gdp_list["gdp"])

# TODO: Создай функцию average_inflation(inflation_list)
# которая считает среднюю инфляцию
def average_inflation(inflation_list):
    """Считает среднюю инфляцию"""
    return sum(inflation_list["inflation"])/len(inflation_list["inflation"])

# TODO: Создай функцию is_growing(gdp_list)
# которая возвращает True, если экономика растет (последний год > первого)

# TODO: Создай функцию health_index(gdp_growth, inflation)
# которая считает индекс здоровья экономики

# TODO: Создай функцию analyze_country(country_data)
# которая принимает словарь страны и возвращает анализ (средние, рост, здоровье)
