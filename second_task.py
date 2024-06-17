"""Друге завдання"""

import random


def get_numbers_ticket(min, max, quantity):
    """Параметри функції набувають таких обмежень:
       1. min - не менше 1;
       2. max - не більше 1000.
       Поверне відсортований список випадкових цифр
                                від min до max включно, розміром quantity"""
    if min < 1 or max > 1000:
        return 'Вхідні параметри не відповідають заданим обмеженням'
    else:
        population = range(min, max + 1)
        res = random.sample(population, k=quantity)
        return sorted(res)
