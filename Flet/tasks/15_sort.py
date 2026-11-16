# Практика 15 — Сортировка, выбор и работа с коллекциями
# ЗАДАЧА: Рейтинг видеоигр
# Откройте соответствующий lessons/15_sort.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

'''
Добавьте массив минимум из 6 игр с id, названием и оценкой.
Dropdown: сортировка по названию или оценке.
Switch: сортировка в обратном порядке.
По клику на кнопку «Выбрать» возле игры покажите её id; сортировка не должна менять выбор.
'''

import flet as ft

GAMES = [
    {"id": 101, "name": "Portal", "rating": 9.6},
    {"id": 102, "name": "Celeste", "rating": 9.1},
    {"id": 103, "name": "Hades", "rating": 9.4},
    {"id": 104, "name": "GTA 3", "rating": 9.1},
    {"id": 105, "name": "Cars", "rating": 1.0},
    {"id": 106, "name": "Tanks", "rating": 5.4},
]


def main(page: ft.Page):

    order = ft.Dropdown(label="Сортировать", options=[
        ft.DropdownOption(key="name", text="По названию"),
        ft.DropdownOption(key="rating", text="По оценке"),
    ], value="name")

    reverse = ft.Switch(label="Обратный порядок")
    result = ft.Text("Ничего не выбрано")
    cards = ft.Column()

    def render(e=None):
#        cards.controls = [ft.Text(f"{g["name"]}, {g["rating"]}") for g in GAMES]
        sort = sorted(GAMES, key=lambda g: g[order.value], reverse = reverse.value)
#        result.controls = [ft.Text(f"{g['name']}, {g['rating']}") for g in sort]
        # TODO: sorted() и кнопка выбора по id.
        cards.controls.clear()
        for game in sort:
            cards.controls.append(ft.Row([
                ft.Text(f"{game["name"]}, {game["rating"]}"),
                ft.Button("Выбрать", on_click = lambda e, game_id=game['id']: select_game(game_id)),
            ]))
        page.update()

    def select_game(game_id):
        result.value = f"id выбранной игры: {game_id}"
        page.update()

    order.on_select = render
    reverse.on_change = render
    render()
    page.add(order, reverse, cards, result)
    # TODO: доведите список до 6 игр.


if __name__ == "__main__":
    ft.run(main)

'''
    def render(_):
        nonlocal selected_id
        key = order.value
        rev = reverse.value

        # Сортируем список для отображения
        ordered = sorted(GAMES, key=lambda g: g[key], reverse=rev)

        cards.controls.clear()
        for g in ordered:
            # Кнопка сразу запоминает id конкретной игры
            btn = ft.Button(
                "Выбрать",
                on_click=lambda e, gid=g["id"]: set_selected(gid)
            )
            cards.controls.append(ft.Row([ft.Text(f"{g['name']} — {g['rating']}"), btn]))

        if selected_id is None:
            result.value = "Ничего не выбрано"
        else:
            game = next(g for g in GAMES if g["id"] == selected_id)
            result.value = f"Выбрана игра: id {game['id']} — {game['name']}"
        page.update()
'''