# Практика 13 — Card, ListTile и изображения
# ЗАДАЧА: Каталог компьютерных комплектующих
# Откройте соответствующий lessons/13_cards.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.
'''
Подготовьте список из четырёх комплектующих с названием, ценой и остатком.
Для каждой записи сформируйте Card c иконкой, названием и ценой.
Отдельно выделите остаток, если он равен нулю.
Организуйте карточки вертикально, без горизонтального переполнения.
'''

'''

'''

import flet as ft

PRODUCTS = [
    {"name": "SSD 512 ГБ", "price": 4200, "stock": 7, "icon": ft.Icons.STORAGE},
    {"name": "ОЗУ 16 ГБ", "price": 3100, "stock": 0, "icon": ft.Icons.MEMORY},
    {"name": "Мышь", "price": 890, "stock": 18, "icon": ft.Icons.MOUSE},
    {"name": "Клавиатура", "price": 2200, "stock": 3, "icon": ft.Icons.KEYBOARD},
]


def main(page: ft.Page):
    page.title = "Комплектующие"
    cards = ft.Column(spacing=10)
    
    for product in PRODUCTS:
        color=ft.Colors.GREEN
        if product["stock"] == 0:
            color = ft.Colors.RED
        

        cards.controls.append(ft.Card(content=ft.Container(padding=12, bgcolor=color, content=ft.Row(controls=[
            ft.Icon(product['icon']),
            ft.Text(f'{product["name"]}, Цена:{product["price"]}, В наличии:{product["stock"]}')
    ]))))
    page.add(cards)
    # TODO: иконка, цена, остаток и условное выделение.


if __name__ == "__main__":
    ft.run(main)
