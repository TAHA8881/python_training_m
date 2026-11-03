# Практика 11 — Динамическое добавление и удаление элементов
# ЗАДАЧА: Список фильмов «Посмотреть»
# Откройте соответствующий lessons/11_dynamic.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft


def main(page: ft.Page):
    movies = ["Интерстеллар", "Контакт", "Начало"]
    new_movie = ft.TextField(label="Новый фильм")
    movie_list = ft.Column()

    def redraw():
        movie_list.controls = [ft.Text(name) for name in movies]
        # TODO: у каждой строки должна быть собственная кнопка удаления.

    def add_movie(e):
        # TODO: добавление с проверкой пустой строки.
        pass

    redraw()
    page.add(new_movie, ft.Button("Добавить", on_click=add_movie), movie_list)


if __name__ == "__main__":
    ft.run(main)
