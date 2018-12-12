from tkinter import *
from tkinter import ttk
from Entities.Tournament import Tournament
from BusinessLayer.BusinessLayerTournament import BusinessLayerTournament
from UserLayer.formTeam import FormTeam

blt = BusinessLayerTournament()

class FormTournament:
    def __init__(self):
        self.window = Tk()
        self.window.title('Listado de Torneos')
        self.tree = ttk.Treeview(self.window)

        self.actualizarDatos()
        self.tree["columns"]=("name","team_number")
        self.tree.heading('#0', text="Id")
        self.tree.column("name", width=150)
        self.tree.heading("name", text="Nombre")
        self.tree.column("team_number", width=150)
        self.tree.heading("team_number", text="Cantidad de equipos")

        self.frame = Frame(self.window, width=500, height=100)
        self.frame.grid(row=2, column=1, columnspan=3)

        self.button_save = Button(self.frame, text='Crear torneo', command=self.create_tournament)
        self.button_save.pack(side=LEFT, padx=6, pady=2)

        self.button_delete = Button(self.frame, text='Eliminar torneo', fg="red", command=self.delete_tournament)
        self.button_delete.pack(side=LEFT, padx=6, pady=2)

        self.button_update = Button(self.frame, text='Editar torneo', command=self.update_tournament)
        self.button_update.pack(side=LEFT, padx=6, pady=2)

        self.tree.grid(row=1, column=1)
        self.window.mainloop()

    def create_tournament(self):
        def abort():
            form.destroy()

        def save():
            noti = Toplevel()
            tourna = Tournament(None, name.get(), number_teams.get())
            try:
                tournament = blt.create(tourna)
                self.actualizarDatos()
                noti.destroy()
                FormTeam(tournament)
                form.destroy()

            except Exception as e:
                Label(master=noti, text=e).grid(row=0, column=0)

        form = Toplevel()
        form.minsize(280,80)
        form.title('Datos del Torneo')

        label_nom = Label(form, text="Nombre del torneo")
        label_nom.grid(row=0, column=0)
        label_number_teams = Label(form, text="Cantidad de equipos")
        label_number_teams.grid(row=1, column=0)

        frame = Frame(form, width=50, height=10)
        frame.grid(row=4, column=1, columnspan=1)

        accept = Button(frame, text="Guardar", command=save)
        accept.pack(side="left")
        abort = Button(frame, text="Cancelar", command=abort)
        abort.pack(side="left")

        #Variables
        name = StringVar()
        number_teams = IntVar()

        e_name = Entry(form, textvariable=name)
        e_name.grid(row=0, column=1)
        e_number_teams = Entry(form, textvariable=number_teams)
        e_number_teams.grid(row=1, column=1)

    def delete_tournament(self):
        noti = Toplevel()
        selection = self.tree.selection()
        selectedTournament = self.tree.item(selection)
        try:
            blt.delete(selectedTournament['text'])
            self.tree.delete(*self.tree.get_children())
            self.actualizarDatos()
            Label(master=noti, text='torneo eliminado.').grid(row=0, column=0)
        except Exception as e:
            Label(master=noti, text=e).grid(row=0, column=0)

    def update_tournament(self):
        def abort():
            form.destroy()

        def save():
            noti = Toplevel()
            try:
                blt.update(Tournament(tournament.id, name.get(), tournament.contestants))
                self.actualizarDatos()
                noti.destroy()
                form.destroy()

            except Exception as e:
                Label(master=noti, text=e).grid(row=0, column=0)

        form = Toplevel()

        label_nom = Label(form, text="Nuevo nombre del torneo")
        label_nom.grid(row=0, column=0)

        frame = Frame(form, width=50, height=10)
        frame.grid(row=4, column=1, columnspan=1)

        accept = Button(frame, text="Guardar", command=save)
        accept.pack(side="left")
        abort = Button(frame, text="Cancelar", command=abort)
        abort.pack(side="left")

        #Variables

        selection = self.tree.selection()
        selectedTournament = self.tree.item(selection)
        id = selectedTournament['text']

        tournament = blt.get_tournament(id)

        name = StringVar(value=tournament.tournament_name)

        e_name = Entry(form, textvariable=name)
        e_name.grid(row=0, column=1)

    def actualizarDatos(self):
        self.tree.delete(*self.tree.get_children())
        for i in blt.get_all():
            self.tree.insert("", 'end', text=i[0], values=(i[1], i[2]))

FormTournament()



