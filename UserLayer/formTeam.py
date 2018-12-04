from tkinter import *
from tkinter import ttk


class FormTeam:
    def __init__(self, tournament):
        super().__init__()

        self.window = Tk()

        self.tree = ttk.Treeview(self.window)

        self.tree["columns"] = ("name", "team_number")
        self.tree.heading('#0', text="Id")
        self.tree.column("name", width=150)
        self.tree.heading("name", text="Nombre")
        self.tree.column("team_number", width=150)
        self.tree.heading("team_number", text="Cantidad de equipos")

        self.frame = Frame(self.window, width=500, height=100)
        self.frame.grid(row=2, column=1, columnspan=3)

        self.button_save = Button(self.frame, text='Alta')
        self.button_save.pack(side='left')

        self.button_delete = Button(self.frame, text='Baja')
        self.button_delete.pack(side='left')

        self.button_update = Button(self.frame, text='Modificación')
        self.button_update.pack(side='left')

        self.tree.grid(row=1, column=1)

        self.tournament = tournament
        print(tournament)


if __name__ == "__main__":
    root = ttk.Root()
    root.mainloop()
