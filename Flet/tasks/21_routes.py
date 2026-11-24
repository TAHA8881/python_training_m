# Практика 21 — View и маршруты: многоэкранное приложение
# ЗАДАЧА: Маршруты для списка музеев
# Откройте соответствующий lessons/21_routes.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

'''
Сделайте главный маршрут / с кнопками двух музеев.
Реализуйте отдельные страницы /museum/1 и /museum/2.
На страницах деталей показывайте разные описания и AppBar.
Реализуйте корректный возврат назад через page.on_view_pop; проверьте прямой вход по маршруту.
'''

import flet as ft

MUSEUMS = {"1": "Музей космоса", "2": "Музей истории"}


def main(page: ft.Page):
    async def go_to_museum(museum_id: str):
        # TODO: await page.push_route(f"/museum/{museum_id}")
        await page.push_route(f"/museum/{museum_id}")

    def make_button(museum_id: str) -> ft.Button:
        async def open_museum(e):
            await go_to_museum(museum_id)
        return ft.Button(MUSEUMS[museum_id], on_click=open_museum)
    
# TODO: создайте по кнопке для каждого музея.
    def route_changed(e=None):
        page.views.clear()
        page.views.append(ft.View(route="/", controls=[
            ft.Text("Музеи", size=26),
            make_button("1"),
            make_button("2"),
        ]))
# TODO: дополняйте стек View при маршрутах /museum/1 и /museum/2.

        if page.route == "/museum/1":
            page.views.append(ft.View(route="/museum/1", controls=[
                ft.AppBar(title=ft.Text(MUSEUMS["1"])),
                ft.Text("Макеты ракет и скафандры: как человек осваивал космос."),
            ]))
        elif page.route == "/museum/2":
            page.views.append(ft.View(route="/museum/2", controls=[
                ft.AppBar(title=ft.Text(MUSEUMS["2"])),
                ft.Text("Старые карты и фотографии: история города из первых рук."),
            ]))

    async def view_pop(e: ft.ViewPopEvent):
        # Стрелка «Назад» в AppBar: снимаем верхний View
        # и синхронизируем маршрут с новым верхним
        page.views.remove(e.view)
        await page.push_route(page.views[-1].route)

    page.on_route_change = route_changed
    page.on_view_pop = view_pop
    route_changed()


if __name__ == "__main__":
    ft.run(main)
