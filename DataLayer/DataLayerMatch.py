from DataLayer.Connection import Connection
from Entities.Tournament import Tournament


class DataLayerTournament:

    def __init__(self):
        self.con = Connection()

    def create_match(self, tournament):
        query = "INSERT INTO tournament(tournament_name, contestants) values({0},{1})".format(repr(tournament.tournament_name), tournament.contestants)
        self.con.execute(query)
        id = self.con.cur.lastrowid
        return Tournament(id, tournament.tournament_name, tournament.contestants)


