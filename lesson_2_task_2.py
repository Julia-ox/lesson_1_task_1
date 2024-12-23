def is_year_leap(year):
    """
    Проверяет, является ли год високосным.

    :param year: Год (целое число)
    :return: True, если год високосный, иначе False
    """
    return year % 4 == 0

# Пример использования
year = 2024
result = is_year_leap(year)
print(f"год {year}: {result}")

year = 2023
result = is_year_leap(year)
print(f"год {year}: {result}")
