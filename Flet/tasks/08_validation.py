# Практика 08 — Валидация форм и ошибки ввода
# ЗАДАЧА: Проверка регистрации на олимпиаду
# Откройте соответствующий lessons/08_validation.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft


def main(page: ft.Page):
    fio = ft.TextField(label="ФИО")
    course = ft.TextField(label="Курс (1–4)")
    feedback = ft.Text()

    def register(e):
        fio.error_text = None
        course.error_text = None
        # TODO: проверьте длину ФИО, число и допустимый диапазон.
        feedback.value = "Форма ещё не проверена"

    page.add(fio, course, ft.Button("Зарегистрироваться", on_click=register), feedback)


if __name__ == "__main__":
    ft.run(main)
