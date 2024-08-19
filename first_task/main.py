"""Перше завдання"""

from datetime import datetime


def get_days_from_today(date):
    """Функція розраховує кількість днів між заданою датою і поточною датою"""
    try:
        date = datetime.strptime(date, '%Y-%m-%d').date()
        today_date = datetime.today().date()
        difference = today_date - date
        return difference.days
    except ValueError:
        return 'Неправильний формат вхідних даних'
