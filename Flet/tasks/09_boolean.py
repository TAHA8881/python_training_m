# Практика 09 — Checkbox и Switch: логические значения
# ЗАДАЧА: Выбор услуг в мастерской
# Откройте соответствующий lessons/09_boolean.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft


def main(page: ft.Page):
    page.title = "Услуги"
    diagnostics = ft.Checkbox(label="Диагностика", value=False)
    counter = ft.Text("Выбрано: 0")

    def recalc(e):
        # TODO: подсчитайте количество выбранных Checkbox.
        pass

    diagnostics.on_change = recalc
    page.add(diagnostics, counter)
    # TODO: добавьте ещё два Checkbox и Switch.


if __name__ == "__main__":
    ft.run(main)
