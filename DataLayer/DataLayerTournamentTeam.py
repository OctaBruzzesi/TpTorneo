from DataLayer.Connection import Connection
from Entities.TournamentTeam import TournamentTeam


class DataLayerTournamentTeam:

    def __init__(self):
        self.con = Connection()

    def create_tournament_team(self, id_tournament, id_team):
        query = "INSERT INTO tournament_team(id_tournament, id_team) values({0},{1})".format(id_tournament, id_team)
        self.con.execute(query)
        return TournamentTeam(id_tournament, id_team)
