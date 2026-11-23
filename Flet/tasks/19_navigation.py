# Практика 19 — NavigationBar: переключение экранов
# ЗАДАЧА: Мини-приложение городской среды
# Откройте соответствующий lessons/19_navigation.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.
'''
Сделайте разделы «События», «Места» и «Профиль» в нижней панели.
При переключении должна меняться не только надпись, но и набор элементов.
Добавьте в профиле поле имени и кнопку сохранения локального состояния.
На каждом экране оставьте одинаковые отступы и общий стиль.
'''

import flet as ft


def main(page: ft.Page):
    page.title = "Мой город"
    content = ft.Column(controls=[ft.Text("События", size=24)])

    screen_events =ft.Column([
        ft.text("События"),
        ft.Text
    ])

    def show_screen(e):
        # TODO: отображайте разные элементы в зависимости от selected_index.
        titles = ["События", "Места", "Профиль"]
        content.controls = [ft.Text(titles[e.control.selected_index], size=26)]

    page.navigation_bar = ft.NavigationBar(destinations=[
        ft.NavigationBarDestination(icon=ft.Icons.EVENT, label="События"),
        ft.NavigationBarDestination(icon=ft.Icons.PLACE, label="Места"),
        ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Профиль"),
    ], on_change=show_screen)
    page.add(content)


if __name__ == "__main__":
    ft.run(main)
