from tkinter import *
from tkinter import ttk
from UserLayer.formTournament import FormTournament
from BusinessLayer.BusinessLayerMatch import BusinessLayerMatch
from BusinessLayer.BusinessLayerTournament import  BusinessLayerTournament
from BusinessLayer.BusinessLayerTeam import BusinessLayerTeam

blm = BusinessLayerMatch()
blt = BusinessLayerTournament()
bltm = BusinessLayerTeam()

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

            tree = ttk.Treeview(vista)

            tree["columns"] = ("name_team")
            tree.heading('#0', text="Nombre del torneo")
            tree.column("name_team", width=150)
            tree.heading("name_team", text="Nombre del Equipo")
            tree.pack()

            finals = blm.get_finals()
            for i in finals:
                tournament = blt.get_tournament(i.id_tournament)
                if i.score_team_1 > i.score_team_2:
                    team_win = bltm.get_team(i.team_1)
                else:
                    team_win = bltm.get_team(i.team_2)
                tree.insert('', 'end', text=tournament.tournament_name, values=team_win.team_name)

        def pending_tournaments():
            vista = Toplevel()

            tree = ttk.Treeview(vista)

            tree["columns"] = ("name_team")
            tree.heading('#0', text="Id Torneo")
            tree.column("name_team", width=150)
            tree.heading("name_team", text="Nombre del Torneo")
            tree.pack()
            pendings = blm.get_pendings()
            for i in pendings:
                tournament = blt.get_tournament(i[0])
                tree.insert('', 'end', text=tournament.id, values=tournament.tournament_name)



        form = Toplevel()
        button = ttk.Button(form, text="Equipos Campeones", command=tournaments_win)
        button.pack()
        button2 = ttk.Button(form, text="Torneos no finalizados", command= pending_tournaments)
        button2.pack(pady=10, padx=125)


    def open_tournament(self):
        FormTournament()

Menu()
