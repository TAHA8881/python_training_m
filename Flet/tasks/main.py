
import flet as ft

def main(page: ft.Page):
    page.title = "Бейдж"
    page.padding = 24
    
    page.add(ft.Container(
        width=1200,
        padding=20, margin=10, border_radius=16,
        bgcolor=ft.Colors.WHITE,
        shadow = ft.BoxShadow(
            blur_radius = 15,
            color= ft.Colors.BLACK_12
        ),

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
                    content=ft.Icon(ft.Icons.IMAGE, size=200),
                    width=200,
                    
                ),
                
            
                ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Container(
                            width=110,
                            padding=7, margin=15, border_radius=16,
                            bgcolor=ft.Colors.LIGHT_BLUE_50,
                            content = ft.Text("Детская обувь", color=ft.Colors.BLUE)
                        ),
                        ft.Container(
                            width=80,
                            padding=5, margin=15, border_radius=16,
                            bgcolor=ft.Colors.BLACK_12,
                            content = ft.Text("Кросовки", color=ft.Colors.BLACK)
                        )
                    ]),    
                    ft.Text('Кросовки детские "Звёздочка" экокожа', size=22, weight=ft.FontWeight.BOLD),
                    ft.Text("Производитель: Малыш-Спорт"),
                    ft.Text('Кросовки детские "Звёздочка экокожа". Производитель: OOO Малыш-Спорт, г.Смоленск'),
                    ft.Container(
                        width=600,
                        padding=5, margin=15, border_radius=16,
                        bgcolor=ft.Colors.BLACK_12,
                        content =ft.Column(controls=[
                            ft.Text("СОСТАВ", color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
                            ft.Text("Верх - экокожа(полуретан на хлопковой основе),подкладка - хлопок 100%,подошва - ПВХ", color=ft.Colors.BLACK)
                        ])
                    )
#            )
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
            ),

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