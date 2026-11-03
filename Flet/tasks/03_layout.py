# Практика 03 — Row и Column: сборка макетов
# ЗАДАЧА: Шапка сайта библиотеки
# Откройте соответствующий lessons/03_layout.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.
'''
Слева расположите иконку книги и название «Электронная библиотека».
Справа в той же строке разместите текст «Каталог | Мои книги».
Под шапкой добавьте заголовок раздела и описание в Column.
Настройте отступы и расстояния между элементами.

'''
import flet as ft


def main(page: ft.Page):
    page.title = "Электронная библиотека"
    page.padding = 24
#    header = ft.Row(controls=[ft.Text("Электронная библиотека")])
#    page.add(ft.Column(controls=[header, ft.Text("Раздел")], spacing=20))
    # TODO: соберите настоящую шапку из Row и вложенных Column.
    page.add(ft.Row(controls=[
        ft.Icon(ft.Icons.BOOK),
        ft.Text("Электронная библиотека", weight=ft.FontWeight.BOLD, size=30),
        ft.Column(spacing=2, controls=[
            ft.Text("Каталог | Мои книги", size=20),
        ]),
    ], spacing=12))

    page.add(ft.Column(controls=[
        ft.Text("Математика", weight=ft.FontWeight.BOLD, size=20),
        ft.Text("Она очень важна", size=16),]))

if __name__ == "__main__":
    ft.run(main)
