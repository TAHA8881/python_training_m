# Практика 10 — Dropdown и Slider: выбор одного значения
# ЗАДАЧА: Конфигуратор сложности теста
# Откройте соответствующий lessons/10_choice.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft


def main(page: ft.Page):
    page.title = "Генератор теста"
    mode = ft.Dropdown(label="Режим", options=[
        ft.DropdownOption(key="practice", text="Тренировка"),
    ])
    result = ft.Text("Тест не настроен")
    page.add(mode, ft.Button("Создать тест"), result)
    # TODO: добавьте ещё 2 режима, Slider и обработчик кнопки.


if __name__ == "__main__":
    ft.run(main)
    