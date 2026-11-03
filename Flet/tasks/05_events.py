# Практика 05 — Кнопки и обработчики событий
# ЗАДАЧА: Пульт светового сигнала
# Откройте соответствующий lessons/05_events.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

'''
Создайте индикатор «Сигнал выключен».
Добавьте кнопки «Включить» и «Выключить».
Свяжите кнопки с разными обработчиками; изменяйте подпись и её цвет.
Добавьте кнопку «Сброс» и верните исходное состояние.
'''

import flet as ft


def main(page: ft.Page):
    page.title = "Пульт"
    status = ft.Text("Ожидание", size=24, color=ft.Colors.BLACK)

    def turn_on(e):
        status.value = "Сигнал включён"
        status.color = ft.Colors.GREEN
        page.update()

    def turn_off(e):
        status.value = "Сигнал выключён"
        status.color = ft.Colors.RED
        page.update()

    def turn_wait(e):
        status.value = "Ожидание"
        status.color = ft.Colors.BLACK
        page.update()
    pass

    page.add(status,
        ft.Row(controls=[
            ft.Button("Включить", on_click=turn_on),
            ft.Button("Выключить", on_click=turn_off),
            ft.Button("Сброс", on_click=turn_wait)
    ]) )

if __name__ == "__main__":
    ft.run(main)
