from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from BusinessLayer.BusinessLayerMatch import BusinessLayerMatch
from BusinessLayer.BusinessLayerTeam import BusinessLayerTeam
from UserLayer.form import Form


blm = BusinessLayerMatch()
blt = BusinessLayerTeam()


class FormMatch(Form):
    def __init__(self, tournament, range_matches):

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
                blm.result(match, score_team_1.get(), score_team_2.get())
                print(match.id_phase)
                if match.id_phase == 1:
                    if score_team_1.get() > score_team_2.get():
                        team_w = team_1.team_name
                    else:
                        team_w = team_2.team_name
                    print(team_w)
                    messagebox.showinfo("Resultado", "El ganador es " + team_w, parent=self.window)
                self.updateView()
                noti.destroy()
                form.destroy()

            except Exception as e:
                Label(master=noti, text=e).grid(row=0, column=0)

        form = Toplevel()
        form.title('top level 1')

        selectedMatch = super(FormMatch, self).get_select(self.tree)
        match = blm.get_match(selectedMatch)

        team_1 = blt.get_team(match.team_1)
        team_2 = blt.get_team(match.team_2)

        label_score_1 = Label(form, text="Puntaje equipo " + team_1.team_name)
        label_score_1.grid(row=0, column=0)

        label_score_2 = Label(form, text="Puntaje equipo " + team_2.team_name)
        label_score_2.grid(row=1, column=0)

        frame = Frame(form, width=125, height=50)
        frame.grid(row=4, column=1, columnspan=1)

        accept = Button(frame, text="Guardar", command=save)
        accept.pack(side="left")
        abort = Button(frame, text="Cancelar", command=abort)
        abort.pack(side="left")

        # Variables

        score_team_1 = IntVar(value=0)
        score_team_2 = IntVar(value=0)

        e_score_1 = Entry(form, textvariable=score_team_1)
        e_score_1.grid(row=0, column=1)
        e_score_2 = Entry(form, textvariable=score_team_2)
        e_score_2.grid(row=1, column=1)

    def updateView(self):
        self.tree.delete(*self.tree.get_children())
        for i in blm.get_matches(self.tournament, self.range_matches):
            team_1 = blt.get_team(i.team_1)
            team_2 = blt.get_team(i.team_2)
            self.tree.insert("", 'end', text=i.id, values=(team_1.team_name, i.score_team_1, i.score_team_2, team_2.team_name))
