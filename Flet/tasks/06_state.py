# Практика 06 — Состояние приложения и обновление UI
# ЗАДАЧА: Счётчик свободных мест
# Откройте соответствующий lessons/06_state.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.
'''
Начальное количество мест — 12.
Реализуйте кнопки «Занять 1» и «Освободить 1».
Не допускайте значения меньше 0 и больше 12.
Вынесите изменение текста и цвета в отдельную функцию render().
'''

import flet as ft


def main(page: ft.Page):
    seats = 12
    max_seats = 12
    available = ft.Text(f"Свободно: {seats}", size=24)

    def render():
        # TODO: единое место обновления интерфейса.
        available.value = f"Стульев: {seats} шт."


    def reserve(e):
        nonlocal seats
        # TODO: уменьшить seats без выхода за границы и вызвать render.
        seats = max(0, seats - 1)
        render()

    def leave(e):
        nonlocal seats
        # TODO: уменьшить seats без выхода за границы и вызвать render.
        seats = min(max_seats, seats + 1)
        render()


    page.add(available, 
            ft.Row(controls=[
                ft.Button("Занять 1", on_click=reserve),
                ft.Button("Освободить 1", on_click=leave)
            ])
        )
    # TODO: реализуйте освобождение места.

    render()

if __name__ == "__main__":
    ft.run(main)
