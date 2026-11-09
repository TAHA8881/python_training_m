# Практика 11 — Динамическое добавление и удаление элементов
# ЗАДАЧА: Список фильмов «Посмотреть»
# Откройте соответствующий lessons/11_dynamic.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.
'''
Задайте начальный список минимум из трёх фильмов.
Добавьте поле для ввода названия и кнопку «Добавить фильм».
Пустое название добавляться не должно.
Реализуйте кнопку удаления у каждого фильма; перерисовывайте список по данным.
'''

import flet as ft


def main(page: ft.Page):
    movies = ["Интерстеллар", "Контакт", "Начало"]
    new_movie = ft.TextField(label="Новый фильм")
    movie_list = ft.Column()
 

    def redraw():
#        movie_list.controls = [ft.Text(name) for name in movies]
        # TODO: у каждой строки должна быть собственная кнопка удаления.
        movie_list.controls.clear()
        for i in range(len(movies)):
            movie_list.controls.append(
                ft.Row([
                    ft.Text(movies[i]),
                    ft.Button(f"Удалить{i+1}", on_click = lambda e, idx = 1:
                              dell_movie[idx])
                ])
            )



    def dell_movie(index):
        # TODO: добавление с проверкой пустой строки.
        del movies[index]
        redraw()

    def add_movie(e):
        # TODO: добавление с проверкой пустой строки.
        if new_movie.value.strip():
            movies.append(new_movie.value.strip())
            redraw()

    page.add(new_movie, ft.Button("Добавить", on_click=add_movie), movie_list)


if __name__ == "__main__":
    ft.run(main)
