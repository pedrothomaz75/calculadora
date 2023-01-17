import tkinter as tk
from typing import List


""" Setando as configurações da janela """
def make_root():
    root = tk.Tk()
    root.title('Calculadora')
    root.config(padx=10, pady=10, background='#000000')
    root.resizable(False, False)
    return root


""" Criando o label de resultado de conta e histórico de conta """
def make_label(root) -> tk.Label:
    label = tk.Label(
        root, text='Sem conta ainda',
        # Joga a label pro lado direito e deixa ela fixa lá
        anchor= 'e', 
        # Justificar ele a direita
        justify='right', background='#ccc',
        )

    """Juntando a label com o grid """
    # A grid começa na linha0, coluna 0 e se estende em 5 colunas
    label.grid(row=0, column=0, columnspan=5, sticky='news') # NEWS = NORTH, EAST, WEST, SOUTH
    return label

def make_display(root) -> tk.Entry:
    display = tk.Entry(root) # Colocando o root na janela principal
    display.grid(row=1, column=0, columnspan=5, sticky='news', pady=(0, 10))
    display.config(
        font=('Helvetica', 40, 'bold'),
        justify='right', bd=1, relief='flat',
        highlightthickness=1, highlightcolor='#ccc',
    )
    display.bind('<Control-a>', display_control_a) # Vai capturar todo evento qur for feito dentro da janela, recebendo parâmetros de entrada
    return display

def display_control_a(event):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
    return 'break'


def make_buttons(root) -> List[List[tk.Button]]:
    button_texts: List[List[str]] = [
        ['7', '8', '9', '+', 'C'],
        ['4', '5', '6', '-', '/'],
        ['1', '2', '3', '*', '^'],
        ['0', '.', '(', ')', '='],
    ]

    buttons: List[List[tk.Button]] = []

    for row,row_value in enumerate(button_texts, start=2):
        button_row = []
        for col_index, col_value in enumerate(row_value):
            btn = tk.Button(root, text=col_value)
            btn.grid(row=row, column=col_index, sticky='news', padx=5, pady=5)
            # Expande a grid de acordo com os botões
            btn.config(
                font=('Helvetica', 15, 'normal'),
                pady=40, width=1, background='#FFA500', bd=0,
                cursor='hand2', highlightcolor='#4F4F4F',
                highlightthickness=0, activebackground='#4F4F4F',
                highlightbackground='#4F4F4F',
            )
            button_row.append(btn)
        buttons.append(button_row)
    return buttons