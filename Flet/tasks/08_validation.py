# Практика 08 — Валидация форм и ошибки ввода
# ЗАДАЧА: Проверка регистрации на олимпиаду
# Откройте соответствующий lessons/08_validation.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.
'''
Создайте поля «ФИО» и «Курс обучения».
ФИО должно быть не короче трёх символов.
Курс — целое число от 1 до 4; ловите ValueError.
Показывайте ошибки возле соответствующих полей и очищайте их после исправления.
'''

import flet as ft


def main(page: ft.Page):
    fio = ft.TextField(label="ФИО")
    course = ft.TextField(label="Курс (1–4)")
    feedback = ft.Text()

    def register(e):
        course.error = None
        fio.error = None
        feedback.value = ""

        try:
            fio_value = (fio.value or "")
            fio_len = len(fio_value)
            if fio_len < 3:     
                raise ValueError
        except ValueError:
            fio.error = "Что то пошло не так"
            feedback.value = f"Введите ФИО, оно болжно быть больше 3 букв"

#-------------------------------------------------------

        course.error = None
        try:
            amount_2 = int(course.value)
            if not 1 <= amount_2 <= 4:
                raise ValueError
        except ValueError:
            course.error = "Что то пошло не так"
            feedback.value = f"Введите курс, он болжен быть 1–4"
        # TODO: проверьте длину ФИО, число и допустимый диапазон.
        if course.error is None and fio.error is None:
            feedback.value = "Регистрация успешна"


    page.add(fio, course, ft.Button("Зарегистрироваться", on_click=register), feedback)


if __name__ == "__main__":
    ft.run(main)
'''

import flet as ft

def main(page: ft.Page):
    price = ft.TextField(label="Цена, ₽")
    output = ft.Text()

    def calculate(e):
        price.error_text = None
        try:
            amount = float((price.value or "").replace(",", "."))
            if amount < 0:
                raise ValueError
            output.value = f"С НДС 20%: {amount * 1.2:.2f} ₽"
        except ValueError:
            price.error_text = "Введите неотрицательное число"
            output.value = ""

    page.add(price, ft.Button("Рассчитать", on_click=calculate), output)

ft.run(main)
'''