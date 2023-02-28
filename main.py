from tkinter import *
from tkinter import ttk
from table import MyTable
from dataHandler import HandlerDB as Db
from manage import ViewCard
from mainLayout import Layout as Lay


class MainWindow:
    """Janela principal da aplicacao"""
    texts: list[str] = ['Tablela', 'Cadastro']
    _handler = Db()

    def __init__(self):
        self.window = Tk()
        self.window.geometry('800x600')
        self.frm_00 = Frame(self.window)

        self.menubar = Menu(self.frm_00)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.editmenu = Menu(self.menubar, tearoff=0)

        self.add_cascade_(self.menubar, 'Tabelas')
        self._names: dict = self.request_table_names()
        self.filemenu.add_separator()

        for _table in self._names.keys():
            self.add_command(self._names[_table], _table)
            self.window.configure(menu=self.menubar)

        self.frm_00.pack()

    def add_cascade_(self, menu: Menu, text: str):
        """Definindo Nomes no menu da camada superior
        <param> >menu<: objeto Menu a receber a lista
        <param> >text<: texto de exibicao da lista"""

        menu.add_cascade(
            label=text,
            menu=self.filemenu,
            command=lambda: self.add_command(text),
            activebackground='black',
            activeforeground='green'
        )

    def add_command(self, nome: str, arg_name=None):
        """Definindo Nomes no menu da camada inferior
        <param> >nome<: texto de exibicao"""
        self.filemenu.add_command(
            label=nome,
            command=lambda x='About Me Here':
            MyTable(arg_name)
        )

    def request_table_names(self) -> dict:
        """requisitando e formatando os nomes das tableas existentes
        <:return dict column|data"""

        _table_names: list = self._handler.query_request_tables()
        _format_tables: list = self._handler.format_table_names(_table_names)

        dict_table = dict(zip(  # empacotando os dados em chaves:valores
            _table_names, _format_tables))

        return dict_table


class ContainerView(MainWindow):
    cards = ViewCard.layers

    def __init__(self):
        super().__init__()

        self.container = Frame(self.frm_00)
        self.label_0 = Label(self.container, text="Uma Label Aqui")
        self.label_0.pack()
        self.create_combo()
        self.container.pack(expand=1, fill='both')
        self.text_tables = StringVar(self.window)
        self.text_vendors = StringVar(self.window)
        self.diagram = dict()
        self.create_view()
        self.window.mainloop()

    def create_view(self):
        for card in self.cards:  # percorrendo os dados de layout arquivo cellNames.json
            frm = Frame(self.frm_00)
            # filtrando nomes dos cards (adicione ou remova cards na variavel de classe _exclude_cards)
            Lay.creat_lay(frm, self.cards[card], 'label', data=self.request_table_names())
            frm.pack(expand=1, fill='both')

    def create_combo(self):
        # Lay.creat_lay(self.frm_00, self.cards['celNomesL0'], 'label')
        self.text_tables = StringVar()
        self.text_vendors = StringVar()
        list_table = ttk.Combobox(
            self.frm_00,
            textvariable=self.text_tables,
            exportselection=True,
            values=list(self._names.values()),)
        list_table.pack(side='left', expand=True, fill='both')
        list_table.bind('<<ComboboxSelected>>', self.combo_command)

    def combo_command(self, event):
        print(f"texto: {self.text_tables.get()}\nEvento: {event}")


if __name__ == "__main__":
    ContainerView()
