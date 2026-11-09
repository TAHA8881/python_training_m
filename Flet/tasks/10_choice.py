# Практика 10 — Dropdown и Slider: выбор одного значения
# ЗАДАЧА: Конфигуратор сложности теста
# Откройте соответствующий lessons/10_choice.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.
'''
Создайте Dropdown с режимами «Тренировка», «Контроль», «Экзамен».
Добавьте Slider: количество вопросов от 5 до 30 с шагом 5.
Покажите выбранные значения при нажатии «Создать тест».
Проверьте поведение, когда режим не выбран.+
'''

import flet as ft


def main(page: ft.Page):
    page.title = "Генератор теста"
    mode = ft.Dropdown(label="Режим", options=[
        ft.DropdownOption(key="practice", text="Тренировка"),
        ft.DropdownOption(key="practice", text="Контроль"),
        ft.DropdownOption(key="practice", text="Экзамен"),
    ])
    size = ft.Slider(min=5, max=30, value=16, divisions=5)
    result = ft.Text("Тест не настроен")

    # TODO: добавьте ещё 2 режима, Slider и обработчик кнопки.
    def show(e):
        result.value = f"Режим: {mode.value}, размер: {size.value:.0f}"
        
    page.add(mode, size, ft.Button("Создать тест", on_click=show), result)

if __name__ == "__main__":
    ft.run(main)
