# Практика 18 — SnackBar и AlertDialog: обратная связь
# ЗАДАЧА: Подтверждение удаления профиля
# Откройте соответствующий lessons/18_dialogs.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.
'''
Сделайте кнопку «Удалить профиль» в отдельной карточке.
По нажатию откройте AlertDialog с вопросом и двумя кнопками.
При отмене закройте окно без изменения профиля.
При подтверждении измените надпись на странице и покажите SnackBar.
'''

import flet as ft


def main(page: ft.Page):
    page.title = "Профиль"
    status = ft.Text("Профиль существует")

    def delete_close(e):
        status.value = "Профиль не существует"
        page.pop_dialog()
        page.update()
        

    def request_delete(e):
        # TODO: открыть AlertDialog с кнопками «Удалить» и «Отмена».
        dialog_window = ft.AlertDialog(ft.Container(content=
            ft.Column(    
                controls=[
                    ft.Text("Внимание! Нужно добавить подтверждение"),
                    ft.Button("Удалить", on_click=delete_close),
                    ft.Button("«Отмена»", on_click=lambda e: page.pop_dialog())
                ]                                     
            )
        )
        )
        page.show_dialog(ft.SnackBar(ft.Text("Изменения сохранены")))
        page.show_dialog(dialog_window)
        
    page.add(status, ft.Button("Удалить профиль", on_click=request_delete))


if __name__ == "__main__":
    ft.run(main)
