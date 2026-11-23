# Практика 14 — Поиск и фильтрация данных
# ЗАДАЧА: Каталог курсов с фильтром по названию
# Откройте соответствующий lessons/14_filter.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.
'''
Создайте список 8 курсов: название и уровень (начальный/продвинутый).
Сделайте живой поиск по названию курса.
Добавьте Checkbox «Только начальные».
Обновляйте карточки при любом изменении фильтров, не изменяя исходные данные.
'''

import flet as ft

COURSES = [
    {"name": "Python Start", "level": "Начальный"},
    {"name": "SQL Basics", "level": "Начальный"},
    {"name": "API Design", "level": "Продвинутый"},
    {"name": "Async Python", "level": "Продвинутый"},
    {"name": "Введение в AI", "level": "Начальный"},
    {"name": "Машинное обучение", "level": "Продвинутый"},
    {"name": "Веб-разработка", "level": "Начальный"},
    {"name": "Базы данных SQL", "level": "Продвинутый"},
]


def main(page: ft.Page):
    search = ft.TextField(label="Поиск")
    only_easy = ft.Checkbox(label="Только начальные")
    cards = ft.Column()

    def render(e=None):
        cards.controls = [ft.Text(c["name"]) for c in COURSES]
        # TODO: отфильтруйте список по двум условиям.
        if not cards.controls:
            cards.controls = [ft.Text("Совпадений нет")]
        q = search.value.lower()
        filtered = [c for c in COURSES if q in c["name"].lower()]
        if only_easy.value:
            filtered = [c for c in filtered if c["level"] == "Начальный"]
        cards.controls = [ft.Text(c["name"]) for c in filtered] or [ft.Text("Совпадений нет")]

    search.on_change = render
    only_easy.on_change = render
    render()
    page.add(search, only_easy, cards)
    # TODO: расширьте данные хотя бы до 8 курсов.


if __name__ == "__main__":
    ft.run(main)
