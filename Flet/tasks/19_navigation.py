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
    content = ft.Column(controls=[ft.Text("События", weight=ft.FontWeight.BOLD, size=24)])

    events =ft.Column([
        ft.Text("События", weight=ft.FontWeight.BOLD, size=24),
        ft.Text("Концерт"),
        ft.Text("Выставка"),
    ])

    places =ft.Column([
        ft.Text("Места", weight=ft.FontWeight.BOLD, size=24),
        ft.Text("Парк"),
        ft.Text("Метро"),
    ])

    user =ft.Column([
        ft.Text("Профиль", weight=ft.FontWeight.BOLD, size=24),
        ft.TextField("Ваше имя: "),
    ])
    save_button = ft.Button("Сохранить")
    
    show = ft.Column([user, save_button])

    def show_screen(e):
#        # TODO: отображайте разные элементы в зависимости от selected_index.
#        titles = ["События", "Места", "Профиль"]
#        content.controls = [ft.Text(titles[e.control.selected_index], size=26)]

        index= e.control.selected_index
        if index == 0:
            content.controls = [events]
        elif index ==1:
            content.controls = [places]
        elif index ==2:
            content.controls = [show]
        page.update()

    page.navigation_bar = ft.NavigationBar(destinations=[
        ft.NavigationBarDestination(icon=ft.Icons.EVENT, label="События"),
        ft.NavigationBarDestination(icon=ft.Icons.PLACE, label="Места"),
        ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Профиль"),
    ], on_change=show_screen)
    page.add(content)


if __name__ == "__main__":
    ft.run(main)
