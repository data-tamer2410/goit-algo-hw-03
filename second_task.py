"""Друге завдання"""

import random


def get_numbers_ticket(min_num, max_num, quantity):
    """Параметри функції набувають таких обмежень:
       1. min_num - не менше 1;
       2. max_num - не більше 1000.
       Поверне відсортований список випадкових цифр
                                від min до max включно, розміром quantity"""
    population = range(min_num, max_num + 1)
    if any((min_num < 1, max_num > 1000, min_num > max_num,
            quantity > len(population))):
        return []
    else:
        res = random.sample(population, k=quantity)
        return sorted(res)
