import re
from typing import Callable

def generator_numbers(text: str) -> list:
    # формуємо список чисел з рядка - знаходимо числа у форматі з двома знаками після коми, але тип даних чисел - 'str'
    list_numbers = re.findall(r'\d+\.\d{2}', text)
    return list_numbers    


def sum_profit(text: str, generator_numbers: Callable[[str], list]):
    # формуємо список чисел з тексту, використовуючи функцію генератора - результат список чисел у форматі 'str'
    list_num = generator_numbers(text)
    # перетворюємо числа у списку з формату 'str' у формат 'float'
    list_num_float = [float(num) for num in list_num]
    # виводимо суму чисел зі списку
    result = sum(list_num_float)
    return result

# у разі використання функції як модуля для інших файлів - виводити тільки функцію без тестових рядків нижче
if __name__ == '__main__':
    sum_profit()

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

