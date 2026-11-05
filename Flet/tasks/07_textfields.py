# Практика 07 — TextField: ввод и изменение текста
# ЗАДАЧА: Генератор электронного бейджа
# Откройте соответствующий lessons/07_textfields.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.
'''
Добавьте поля «Имя» и «Должность».
По кнопке «Создать бейдж» показывайте готовую подпись из двух полей.
При пустом имени сообщайте пользователю, что его нужно заполнить.
Сделайте должность необязательной.
'''

import flet as ft


def main(page: ft.Page):
    page.title = "Генератор бейджа"
    person = ft.TextField(label="Имя")
    post = ft.TextField(label="Должность")
    result = ft.Text("Бейдж ещё не создан")
    result_2 = ft.Text("Должность ещё не создана")

    def build_badge(e):
        #ft.Column(controls=[
            result.value = (person.value or "").strip() or "Имя не указано",
            result_2.value = (post.value or "").strip(),
        #])


    page.add(person,  post, result, result_2,
             
        ft.Button("Создать бейдж", on_click=build_badge))
    


if __name__ == "__main__":
    ft.run(main)
