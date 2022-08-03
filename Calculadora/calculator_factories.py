import tkinter as tk
from typing import List

def make_root() -> tk.Tk:
    root = tk.Tk()
    root.title('Calculadora')
    root.config(padx=10, pady=10, background='#0a111f')
    root.resizable(False, False)
    return root


def make_label(root) -> tk.Label:
    label = tk.Label(
        root, text='RESULTADO DA EXPRESSÃO:',
        anchor='e', justify='right', background='#0a111f',
        foreground='#fff',
        font=('Verdana', 12)
    )
    label.grid(row=0, column=0, columnspan=5, sticky='news')
    return label


def make_display(root) -> tk.Entry:
    display = tk.Entry(root)
    display.grid(row=1, column=0, columnspan=5, sticky='news', pady=(0, 10))
    display.config(
        font=('Verdana', 40, 'bold'),
        justify='right', bd=0, relief='flat',
        background='#d9d9d9', foreground='#000'
    )
    display.bind('<Control-a>', display_control_a)
    return display


def display_control_a(event):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
    return 'break'

def make_buttons(root) -> List[List[tk.Button]]:
    buttons_texts: List[List[str]] = [
        ['7', '8', '9', '+', 'C'],
        ['4', '5', '6', '-', '/'],
        ['1', '2', '3', '*', '^'],
        ['0', '.', '(', ')', '='],
    ]

    buttons: List[List[tk.Button]] = []

    for row_index, row_value in enumerate(buttons_texts, start=2):
        button_row = []
        for col_index, col_value in enumerate(row_value):
            btn = tk.Button(root, text=col_value)
            btn.grid(row=row_index, column=col_index, sticky='news', padx=5, pady=5)
            btn.config(
                font=('Verdana', 20, 'normal'),
                pady=40, width=1, background='#777777', bd=0,
                cursor='hand2', highlightthickness=0,
                highlightcolor='#ccc', highlightbackground='#ccc',
                activebackground='#adadad', activeforeground='#ffffff',
                fg='#fff'
            )
            button_row.append(btn)
        buttons.append(button_row)
    return buttons




