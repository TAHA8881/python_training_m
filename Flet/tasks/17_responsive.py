# Практика 17 — Адаптивная компоновка ResponsiveRow
# ЗАДАЧА: Дашборд учебной платформы
# Откройте соответствующий lessons/17_responsive.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.
'''
Сделайте 4 карточки метрик: студенты, группы, курсы, тесты.
На узкой ширине показывайте по одной карточке в строке.
На средней — по две, на большой — по четыре.
В каждой карточке используйте заголовок, число и тематическую иконку.
'''
import flet as ft

METRICS = [(ft.Icons.MAN,"Студенты", 128), (ft.Icons.PEOPLE, "Группы", 8), (ft.Icons.BOOK_ONLINE_OUTLINED, "Курсы", 14), (ft.Icons.CHECK_BOX ,"Тесты", 32)]


def main(page: ft.Page):
    page.title = "Показатели"
    cards = []
    for icon, name, count in METRICS:
        cards.append(ft.Container(
            col={ft.ResponsiveRowBreakpoint.XS: 12,
                ft.ResponsiveRowBreakpoint.MD: 6},
            padding=18, bgcolor=ft.Colors.BLUE_50,
            content=ft.Row(
                controls=[
                    ft.Icon(icon),
                    ft.Text(f"{name}: {count}"),
                ]
            ),
        ))
    page.add(ft.ResponsiveRow(controls=cards, spacing=12, run_spacing=12))
    # TODO: breakpoint MD и LG, оформление и иконки.


if __name__ == "__main__":
    ft.run(main)
