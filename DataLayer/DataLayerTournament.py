from DataLayer.Connection import Connection
from Entities.Tournament import Tournament


class DataLayerTournament:

    def __init__(self):
        self.con = Connection()

    def create_tournament(self, tournament):
        query = "INSERT INTO tournament(tournament_name, contestants) values({0},{1})".format(repr(tournament.tournament_name), tournament.contestants)
        self.con.execute(query)
        id = self.con.cur.lastrowid
        return Tournament(id, tournament.tournament_name, tournament.contestants)

    def list_tournaments(self):
        tournaments = []
        query = "Select * From tournament"
        self.con.execute(query)
        t = self.con.cur.fetchall()
        for i in t:
            tournaments.append(i)
        return tournaments

    def update_tournament(self, tournament):
        print(tournament.id, tournament.tournament_name)
        query = "UPDATE tournament set tournament_name = {0} WHERE id_tournament = {1}".format(repr(tournament.tournament_name), tournament.id)
        self.con.execute(query)
        return tournament

    def get_tournament(self, id):
        query = "SELECT * FROM tournament where id_tournament = {0}".format(id)
        self.con.execute(query)
        t = self.con.cur.fetchone()
        tournament = Tournament(t[0], t[1], t[2])
        return tournament

    def delete(self, id):
        query = "DELETE FROM tournament WHERE id_tournament = {0}".format(id)
        self.con.execute(query)


