# Практика 07 — TextField: ввод и изменение текста
# ЗАДАЧА: Генератор электронного бейджа
# Откройте соответствующий lessons/07_textfields.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft


def main(page: ft.Page):
    page.title = "Генератор бейджа"
    person = ft.TextField(label="Имя")
    result = ft.Text("Бейдж ещё не создан")

    def build_badge(e):
        # TODO: проверьте имя, получите должность и измените result.value.
        pass

    page.add(person, result, ft.Button("Создать бейдж", on_click=build_badge))
    # TODO: добавьте поле «Должность».


if __name__ == "__main__":
    ft.run(main)
