# Практика 16 — Тема, цвета и единый визуальный стиль
# ЗАДАЧА: Панель настроек внешнего вида
# Откройте соответствующий lessons/16_theme.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.
'''
Создайте переключатель темы «Светлая/Тёмная».
Добавьте Dropdown из трёх акцентных цветов.
Создайте две карточки-превью с заголовками и текстом.
Убедитесь, что выбранная тема и акцент применяются к обоим превью.
'''
import flet as ft


def main(page: ft.Page):
    page.title = "Внешний вид"
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.BLUE)
    dark = ft.Switch(label="Тёмная тема")

    page.theme_mode = ft.ThemeMode.LIGHT

    def toogle(e):
        preview.bgcolor = dropdown.value

    dropdown = ft.Dropdown(
                width=150,
                options=[
                    ft.dropdown.Option("#F50000", "Red"),
                    ft.dropdown.Option("#04F02B", "Green"),
                    ft.dropdown.Option("#0424DA", "Blue"),
                ],
                on_select=toogle
            )
    preview = ft.Card(content=ft.Container(padding=16, content=ft.Text("Предпросмотр")))


    def apply_settings(e=None):
        # TODO: переключите page.theme_mode.
        dark_is = page.theme_mode == ft.ThemeMode.LIGHT
        page.theme_mode = ft.ThemeMode.DARK if dark_is else ft.ThemeMode.LIGHT
        dark.label = "Тёмная тема" if dark_is else "Светлая тема"

    
        

    dark.on_change = apply_settings
    page.add(dark, preview, dropdown)
    # TODO: Dropdown цветов и второе превью.


if __name__ == "__main__":
    ft.run(main)
