
import flet as ft

def main(page: ft.Page):
    page.title = "Бейдж"
    page.padding = 24
    
    page.add(ft.Container(
        width=1200,
        padding=20, margin=10, border_radius=16,
        bgcolor=ft.Colors.WHITE,

#        tags=ft.Container(
#            padding=20, margin=10, border_radius=16,
#            bgcolor=ft.Colors.BLUE,
#            content=ft.Column(controls=[
#                ft.Row(controls=[
#                ft.Text("Детская обувь", size=2, weight=ft.FontWeight.BOLD),
#                ]),
#                ft.Column(controls=[ft.Text("Студент"),ft.Text("ФК35", weight=ft.FontWeight.BOLD),
#                ]),
#            ]),
#        )

        content=ft.Column(controls=[
            
            ft.Row(controls=[
                ft.Container(
                    content=ft.Icon(ft.Icons.PERSON),
                    width=200,
                    
                ),
                
            
                ft.Column(controls=[
                    ft.Container(
                        width=50,
                        padding=20, margin=10, border_radius=16,
                        bgcolor=ft.Colors.BLUE,
                    ),
                    ft.Text('Кросовки детские "Звёздочка" экокожа', size=22, weight=ft.FontWeight.BOLD),
                    ft.Text("Производитель: Малыш-Спорт"),
                    ft.Text('Кросовки детские "Звёздочка экокожа". Производитель: OOO Малыш-Спорт, г.Смоленск')
                ]),
            ft.Container(
                content= ft.Column(controls=[
                ft.Text('Цена'),
                ft.Text('2 190 P', size=22,  weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE)
            ], alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
                width=200,
                height=200,
                alignment=ft.Alignment.CENTER
            )
            ]),

        ])
    ))

'''
import flet as ft


def main(page: ft.Page):
    page.title = "Бейдж"
    page.padding = 24
    page.add(ft.Container(
        content=ft.Text("Иванов Иван Иванович"),
        padding=12,
        bgcolor=ft.Colors.BLUE_50,
    ))
    # TODO: оформите полноценный бейдж вместо одной надписи.
'''

if __name__ == "__main__":
    ft.run(main)