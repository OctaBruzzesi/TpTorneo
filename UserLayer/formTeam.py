from tkinter import *
from tkinter import ttk
from BusinessLayer.BusinessLayerTeam import BusinessLayerTeam
from Entities.Team import Team


blt = BusinessLayerTeam()

class FormTeam:
    def __init__(self, tournament):

        self.window = Tk()

        self.tree = ttk.Treeview(self.window)

        self.tree["columns"] = ("name")
        self.tree.heading('#0', text="Id")
        self.tree.column("name", width=150)
        self.tree.heading("name", text="Nombre")

        self.frame = Frame(self.window, width=500, height=100)
        self.frame.grid(row=2, column=1, columnspan=3)

        self.button_save = Button(self.frame, text='Alta', command=self.create_team)
        self.button_save.pack(side='left')

        self.button_delete = Button(self.frame, text='Baja')
        self.button_delete.pack(side='left')

        self.button_update = Button(self.frame, text='Modificación')
        self.button_update.pack(side='left')

        self.tree.grid(row=1, column=1)
        self.updateView()
        self.tournament = tournament

        print(tournament)

    def create_team(self):
        def abort():
            form.destroy()

        def save():
            noti = Toplevel()
            team = Team(None, name.get())
            try:
                blt.create(team)
                self.updateView()
                noti.destroy()

            except Exception as e:
                print(e)
                Label(master=noti, text=e).grid(row=0, column=0)
            form.destroy()

        form = Toplevel()

        label_nom = Label(form, text="Nombre del equipo")
        label_nom.grid(row=0, column=0)

        frame = Frame(form, width=50, height=10)
        frame.grid(row=4, column=1, columnspan=1)

        accept = Button(frame, text="Guardar", command=save)
        accept.pack(side="left")
        abort = Button(frame, text="Cancelar", command=abort)
        abort.pack(side="left")

        # Variables
        name = StringVar()
        number_teams = IntVar()

        e_name = Entry(form, textvariable=name)
        e_name.grid(row=0, column=1)


    def updateView(self):
        self.tree.delete(*self.tree.get_children())
        for i in blt.get_all():
            self.tree.insert("", 'end', text=i[0], values=(i[1]))



