# Практика 20 — Tabs, TabBar и TabBarView
# ЗАДАЧА: Вкладки карточки учебного курса
# Откройте соответствующий lessons/20_tabs.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.
'''
Создайте вкладки «Программа», «Преподаватель», «Отзывы».
На первой выведите список тем; на второй — имя и описание преподавателя.
На третьей — 2 отзыва в карточках.
Добавьте в каждую вкладку разные элементы, а не одну изменяемую надпись.
'''
import flet as ft

def main(page: ft.Page):
    page.title = "Курс"
    tabs = ft.Tabs(length=3, expand=True, content=ft.Column(expand=True, controls=[
        ft.TabBar(tabs=[ft.Tab(label="Программа"), ft.Tab(label="Преподаватель"), ft.Tab(label="Отзывы")]),
        ft.TabBarView(expand=True, controls=[
            ft.ListView([
                ft.ListTile(leading=ft.Icon(ft.Icons.CODE), title=ft.Text("Python")),
                ft.ListTile(leading=ft.Icon(ft.Icons.STORAGE), title=ft.Text("SQL")),
                ft.ListTile(leading=ft.Icon(ft.Icons.TABLE_CHART), title=ft.Text("C++")),
            ]),
            ft.Column([
                ft.CircleAvatar(content=ft.Icon(ft.Icons.PERSON, size=40), radius=40),
                ft.Text("Иван Иванович Иванов", size=20, weight=ft.FontWeight.BOLD),
                ft.Text("Преподаватель по программированию, 10 лет опыта",
                        text_align=ft.TextAlign.CENTER),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            ft.Column([
                ft.Card(content=ft.Container(content=ft.Column([
                    ft.Text("Анна, ★★★★★"),
                    ft.Text("Отличный курс! Всё объясняют простым языком."),
                ]))),
                ft.Card(content=ft.Container(content=ft.Column([
                    ft.Text("Дмитрий, ★★★★"),
                    ft.Text("Материал структурирован, много практики."),
                ]))),
            ], spacing=10),
        ]),
    ]))
    page.add(tabs)

if __name__ == "__main__":
    ft.run(main)

'''
import flet as ft


def main(page: ft.Page):
    page.title = "Курс"
    tabs = ft.Tabs(length=2, expand=True, content=ft.Column(expand=True, controls=[
        ft.TabBar(tabs=[ft.Tab(label="Программа"), ft.Tab(label="Преподаватель"), ft.Tab(label="Отзывы")]),
        ft.TabBarView(expand=True, controls=[
            ft.Container(content= ft.Column(
                ft.Text("Темы курса:"), ft.Text("SQL"), ft.Text("Python"), ft.Text("C++"))),
            ft.Container(content= ft.Column(
                ft.Text("Имя преподавателя:"), ft.Text("Иван Иванович Иванов"), ft.Text("Преподаватель по программированию"))),
            ft.Container(content= ft.Column(    
                ft.Text("Отзывы:"), ft.Text("5"), ft.Text("4")))
        ]),
    ]))
    page.add(tabs)
    page.update()
    # TODO: третья вкладка и полноценное содержимое всех вкладок.


if __name__ == "__main__":
    ft.run(main)
'''