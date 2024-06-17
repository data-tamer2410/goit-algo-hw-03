"""Перше завдання"""

from datetime import datetime


def get_days_from_today(date):
    """Функція розраховує кількість днів між заданою датою і поточною датою"""
    try:
        obj_datetime = datetime.strptime(date, '%Y-%m-%d')
        today = datetime.today()
        difference = obj_datetime - today
        return difference.days
    except ValueError:
        return 'Неправильний формат вхідних даних'
