"""Третє завдання"""

import re


def normalize_phone(phone_number):
    """Функція нормалізує телефонні номери до стандартного формату,
                             залишаючи тільки цифри та символ '+' на початку"""
    pattern = r'[^\d\+]'
    clear_phone_number = re.sub(pattern, '', phone_number)
    if clear_phone_number.startswith('38'):
        clear_phone_number = '+' + clear_phone_number
    elif not clear_phone_number.startswith('+38'):
        clear_phone_number = '+38' + clear_phone_number
    return clear_phone_number
