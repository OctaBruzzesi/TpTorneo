from DataLayer.Connection import Connection
from Entities.Tournament import Tournament


class DataLayerTorunament

    def __init__(self):
        self.con = Connection()

    def create_tournament(self, tournament):
            query = "INSERT INTO tournament(tournament_name, contestans) values({0},{1})".format(tournament.torunament_name, repr(tournament.contestants))
            self.con.ejecutar(query)
            id = self.con.cur.lastrowid
            return Tournament(id, tournament.torunament_name, tournament.contestants)
