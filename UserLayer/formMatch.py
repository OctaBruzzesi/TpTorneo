from tkinter import *
from tkinter import ttk
from BusinessLayer.BusinessLayerTournament import BusinessLayerTournament
from BusinessLayer.BusinessLayerTeam import BusinessLayerTeam
from BusinessLayer.BusinessLayerMatch import BusinessLayerMatch
from Entities.Tournament import Tournament
from Entities.Team import Team


blt = BusinessLayerTeam()
blTournament = BusinessLayerTournament()
blm = BusinessLayerMatch()


class FormMatch:
    def __init__(self, tournament, range_matches):

        self.selectedTeams = []
        self.teams = blt.get_all()

        self.window = Tk()

        self.tree = ttk.Treeview(self.window)

        self.tree["columns"] = ("team_1", "score_team_1", "score_team_2", "team_2")
        self.tree.heading('#0', text="Id")
        self.tree.column("team_1", width=150)
        self.tree.heading("team_1", text="Equipo 1")
        self.tree.column("score_team_1", width=150)
        self.tree.heading("score_team_1", text="Puntaje Equipo 1")
        self.tree.column("score_team_2", width=150)
        self.tree.heading("score_team_2", text="Puntaje Equipo 2")
        self.tree.column("team_2", width=150)
        self.tree.heading("team_2", text="Equipo 2")

        self.tree.grid(row=0, column=0)

        self.frame = Frame(self.window, width=150, height=100)
        self.frame.grid(row=1, column=0)

        self.button_save = Button(self.frame, text='Resultado', command=self.result)
        self.button_save.pack(side="left")

        self.tournament = tournament

        self.range_matches = range_matches

        self.updateView()

        self.window.mainloop()

    def result(self):
        def abort():
            form.destroy()

        def save():
            noti = Toplevel()
            noti.title('Resultado')
            try:
                print(type(score_team_1))
                blm.result(match, score_team_1.get(), score_team_2.get())
                self.updateView()
                noti.destroy()
                form.destroy()

            except Exception as e:
                Label(master=noti, text=e).grid(row=0, column=0)

        form = Toplevel()
        form.title('top level 1')

        label_score_1 = Label(form, text="Puntaje equipo 1")
        label_score_1.grid(row=0, column=0)

        label_score_2 = Label(form, text="Puntaje equipo 2")
        label_score_2.grid(row=1, column=0)

        frame = Frame(form, width=125, height=50)
        frame.grid(row=4, column=1, columnspan=1)

        accept = Button(frame, text="Guardar", command=save)
        accept.pack(side="left")
        abort = Button(frame, text="Cancelar", command=abort)
        abort.pack(side="left")

        # Variables

        selection = self.tree.selection()
        selectedMatch = self.tree.item(selection)
        print(selectedMatch)
        match = blm.get_match(selectedMatch['text'])

        score_team_1 = IntVar(value=0)
        score_team_2 = IntVar(value=0)

        e_score_1 = Entry(form, textvariable=score_team_1)
        e_score_1.grid(row=0, column=1)
        e_score_2 = Entry(form, textvariable=score_team_2)
        e_score_2.grid(row=1, column=1)


        print(match.id)

    def updateView(self):
        self.tree.delete(*self.tree.get_children())
        for i in blm.get_matches(self.tournament, self.range_matches):
            self.tree.insert("", 'end', text=i.id, values=(i.team_1, i.score_team_1, i.score_team_2, i.team_2))
