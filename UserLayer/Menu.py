from tkinter import *
from tkinter import ttk
from UserLayer.formTournament import FormTournament
from BusinessLayer.BusinessLayerMatch import BusinessLayerMatch
from BusinessLayer.BusinessLayerTournament import  BusinessLayerTournament
from BusinessLayer.BusinessLayerTeam import BusinessLayerTeam


class Menu:
    def __init__(self):

        self.window = Tk()
        self.window.title('Menu')

        label = ttk.Label(self.window, text="Start Page")
        label.pack(pady=10, padx=125)

        button = ttk.Button(self.window, text="Lista de Torneos", command=self.open_tournament)
        button.pack()

        button2 = ttk.Button(self.window, text="Lista de Equipos")
        button2.pack()

        button3 = ttk.Button(self.window, text="Informes", command=self.reportes)
        button3.pack()

        self.window.mainloop()

    def reportes(self):
        def tournaments_win():

            vista = Toplevel()

            blm = BusinessLayerMatch()
            blt = BusinessLayerTournament()
            bltm = BusinessLayerTeam()

            tree = ttk.Treeview(vista)

            tree["columns"] = ("name_team", "name_tournament")
            tree.heading('#0', text="Id")
            tree.column("name_team", width=150)
            tree.heading("name_team", text="Nombre del Equipo")
            tree.column("name_tournament", width=150)
            tree.heading("name_tournament", text="Nombre del Torneo")

            finals = blm.get_finals()
            for i in finals:
                tournament = blt.get_tournament(i.id_tournament)
                if i.score_team_1 > i.score_team_2:
                    team_win = bltm.get_team(i.team_1)
                else:
                    team_win = bltm.get_team(i.team_2)
                tree.insert("", 'end', text='Equipo', values=team_win.team_name)
                tree.insert("", 'end', text=team_win.team_name, values=tournament.tournament_name)

        form = Toplevel()
        button = ttk.Button(form, text="Torneos Ganadores", command=tournaments_win)

        button.pack()
        button2 = ttk.Button(form, text="sarasa")

        button2.pack()




    def open_tournament(self):
        FormTournament()

Menu()
