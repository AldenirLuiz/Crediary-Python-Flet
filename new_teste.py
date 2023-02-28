import flet as ft

text_var = str()


def main(page: ft.Page):

    page.window_width = 340
    page.window_height = 400
    page.window_max_width = 340
    page.window_max_height = 400
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    text_var = str()
    operation_var = list()
    historical_var = list()

    history_label: ft.Text = ft.Text(
        value=text_var, text_align=ft.TextAlign.LEFT,
        color='green', width=150,
        font_family="Arial", size=30,
    )

    operation_label: ft.Text = ft.Text(
        value=text_var, text_align=ft.TextAlign.RIGHT,
        color='green', width=150,
        font_family="Arial", size=30
    )

    primary_label: ft.Text = ft.Text(
        value=text_var, text_align=ft.TextAlign.RIGHT,
        color='green', width=300,
        font_family="Arial", size=30
    )
    main_numbers = ['123+', '456-', '789x', '.0,÷', ['<<', '=']]
    # page.add(primary_label)

    main_row_numbers: list[
            ft.Row,
            ...] = list()

    for row in main_numbers:
        temp_list_buttons = list()
        for char in row:
            temp_list_buttons.append(
                ft.ElevatedButton(text=char, on_click=lambda x, y=char: onclicked(page, y, x), expand=True)
            )
        main_row_numbers.append(
            ft.Row(temp_list_buttons, alignment=ft.MainAxisAlignment.CENTER)
        )

    main_row_numbers.insert(
        0, ft.Row([primary_label], alignment=ft.MainAxisAlignment.CENTER)
    )

    main_row_numbers.insert(
        0, ft.Row([history_label, operation_label], alignment=ft.MainAxisAlignment.CENTER)
    )

    for row in main_row_numbers:
        page.add(row)

    def onclicked(page, x: str, event):
        global text_var

        if x.isalnum():
            operation_var.insert(0, f'{text_var}')
            text_var += x
        elif x == '<<':
            temp_string = text_var[0:-1]
            text_var = temp_string
        else:
            value_ = sum(operation_var)
            history_label.value = f'{operation_var[0]}+{operation_var[1]} = {value_}'

        operation_label.value = text_var
        primary_label.value = text_var
        page.update()
        print(event)


ft.app(target=main)
