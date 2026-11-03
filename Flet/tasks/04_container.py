# Практика 04 — Container, рамки, отступы и карточки
# ЗАДАЧА: Бейдж участника конференции
# Откройте соответствующий lessons/04_container.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

'''
Создайте прямоугольную карточку с именем, должностью и организацией.
Используйте Container с padding, цветом, закруглением и рамкой.
Добавьте внутри иконку и текст, используя Row и Column.
Оставьте заметный внешний отступ карточки.
'''
import flet as ft

def main(page: ft.Page):
    page.title = "Бейдж"
    page.padding = 24
    page.add(ft.Container(
        padding=20, margin=10, border_radius=16,
        bgcolor=ft.Colors.BLUE_50,
        content=ft.Column(controls=[
            ft.Row(controls=[
                ft.Icon(ft.Icons.PERSON),
                ft.Text("Иванов Иван Иванович", size=22, weight=ft.FontWeight.BOLD),
            ]),
            ft.Column(controls=[ft.Text("Студент"),ft.Text("ФК35", weight=ft.FontWeight.BOLD),
            ]),
        ])
    ))
'''
import flet as ft


def main(page: ft.Page):
    page.title = "Бейдж"
    page.padding = 24
    page.add(ft.Container(
        content=ft.Text("Иванов Иван Иванович"),
        padding=12,
        bgcolor=ft.Colors.BLUE_50,
    ))
    # TODO: оформите полноценный бейдж вместо одной надписи.
'''

if __name__ == "__main__":
    ft.run(main)
