# Практика 12 — ListView и GridView: прокрутка и коллекции
# ЗАДАЧА: Галерея учебных дисциплин
# Откройте соответствующий lessons/12_scroll.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.
'''
Создайте сетку минимум из 12 разноцветных карточек дисциплин.
Используйте GridView с тремя столбцами и прокруткой.
В каждой карточке покажите номер и название дисциплины.
Проверьте поведение в небольшом окне.
'''

import flet as ft


def main(page: ft.Page):
    subjects = ["Python", "SQL", "Flet", "Linux", "Git", "Web", "Go", "API", "Docker", "UI", "Тесты", "БД"]
    grid = ft.GridView(expand=True, runs_count=3, spacing=10, run_spacing=10)
    for index, subjects in enumerate(subjects, start = 1):
        grid.controls.append(ft.Container(
            content=ft.Text(f"{index}. {subjects}"), padding=12, bgcolor=ft.Colors.BLUE_50,
        ))
    page.add(ft.Column(expand=True, controls=[
        ft.Text("Дисциплины", size=24), #grid,
        ft.ListView(controls=grid, expand=True, spacing=4),
    ]))
    # TODO: сделайте три столбца и оформите карточки с номером.


if __name__ == "__main__":
    ft.run(main)
