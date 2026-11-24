# Практика 22 — DataTable: табличные данные и сортировка
# ЗАДАЧА: Табель посещаемости
# Откройте соответствующий lessons/22_tables.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

'''
Сформируйте таблицу минимум на 5 студентов с колонками «Студент», «Пропуски», «Средний балл».
Сделайте значения числами в модели, а не только строками.
Реализуйте сортировку по пропускам (возрастание/убывание).
Разместите таблицу с горизонтальной прокруткой.
'''

import flet as ft

STUDENTS = [
    {"name": "Анна", "absences": 1, "grade": 4.8},
    {"name": "Борис", "absences": 5, "grade": 3.9},
    {"name": "Вера", "absences": 0, "grade": 5.0},
    {"name": "Виталий", "absences": 4, "grade": 3.2},
    {"name": "Григорий", "absences": 3, "grade": 5.0},
]

KEYS = ["name", "absences", "grade"]

def main(page: ft.Page):
    def make_rows():
        return [ft.DataRow(cells=[
            ft.DataCell(ft.Text(s["name"])),
            ft.DataCell(ft.Text(int(s["absences"]))),
            ft.DataCell(ft.Text(float(s["grade"]))),
        ]) for s in STUDENTS]

    def on_sort(e: ft.DataColumnSortEvent):
        table.rows = make_rows(
            sorted(STUDENTS, key=lambda s: s[KEYS[e.column_index]], reverse=not e.ascending)
        )
        page.update()

    table = ft.DataTable(columns=[
        ft.DataColumn(label=ft.Text("Студент")),
        ft.DataColumn(label=ft.Text("Пропуски")),
        ft.DataColumn(label=ft.Text("Средний балл")),
    ], sort_column_index=1,  
        sort_ascending=True,
        rows=make_rows(STUDENTS), #sort = sorted(STUDENTS, key=lambda g: g[table.value], reverse = table.value)
    )
    page.add(ft.Row(scroll=ft.ScrollMode.AUTO, controls=[table]))
    # TODO: третий столбец, больше студентов и обработчик on_sort.


if __name__ == "__main__":
    ft.run(main)

