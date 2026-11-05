# Практика 09 — Checkbox и Switch: логические значения
# ЗАДАЧА: Выбор услуг в мастерской
# Откройте соответствующий lessons/09_boolean.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.
'''
Создайте три Checkbox: диагностика, чистка, установка ПО.
При каждом изменении покажите число выбранных услуг.
Добавьте Switch «Срочный заказ» и выводите его состояние.
Если ничего не выбрано, отображайте «Услуги не выбраны».
'''

import flet as ft


def main(page: ft.Page):
    page.title = "Услуги"
    diagnostics = ft.Checkbox(label="Диагностика", value=False)
    cleaning = ft.Checkbox(label="Чистка", value=False)
    dovnload_po = ft.Checkbox(label="Установка ПО", value=False)

    counter = ft.Text("Выбрано: 0")

    urgent_switch = ft.Switch(label="Срочный заказ", value=False)
    urgent_status = ft.Text("Срочный заказ: выключен")

    def recalc(e):
        count = int(diagnostics.value)+int(cleaning.value)+int(dovnload_po.value)
        if count == 0:
            counter.value = "Услуга не выбрано"
        elif count == 1:
            counter.value = "Услуга 1"
        elif 2 <= count <= 4:
            counter.value = f"Услуги {count}"
        else:
            counter.value = f"Услуги {count}"
        page.update()

    def on_urgent(e):
        urgent_status.value = (
            "Срочный заказ: включен" if urgent_switch.value else "Срочный заказ: выключен"
        )
        page.update()

        # TODO: подсчитайте количество выбранных Checkbox.
        pass

    diagnostics.on_change = recalc
    cleaning.on_change = recalc
    dovnload_po.on_change = recalc
    urgent_switch.on_change = on_urgent

    page.add(diagnostics, cleaning, 
            dovnload_po,
            urgent_status,
            urgent_switch,
            counter)
    # TODO: добавьте ещё два Checkbox и Switch.


if __name__ == "__main__":
    ft.run(main)
