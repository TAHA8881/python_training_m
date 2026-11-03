# Практика 06 — Состояние приложения и обновление UI
# ЗАДАЧА: Счётчик свободных мест
# Откройте соответствующий lessons/06_state.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft


def main(page: ft.Page):
    seats = 12
    available = ft.Text(f"Свободно: {seats}", size=24)

    def render():
        # TODO: единое место обновления интерфейса.
        pass

    def reserve(e):
        nonlocal seats
        # TODO: уменьшить seats без выхода за границы и вызвать render.
        pass

    page.add(available, ft.Button("Занять 1", on_click=reserve))
    # TODO: реализуйте освобождение места.


if __name__ == "__main__":
    ft.run(main)
