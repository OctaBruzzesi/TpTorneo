from DataLayer.Connection import Connection
from Entities.Tournament import Tournament


class DataLayerMatch:

    def __init__(self):
        self.con = Connection()

    def create_match(self, team_1, team_2, id_tournament, id_phase):
        query = "INSERT INTO tournaments.match(team_1, team_2, id_tournament, id_phase) values({0},{1},{2},{3})".format(team_1, team_2, id_tournament, id_phase)
        self.con.execute(query)
        return True

    def create_next_match(self, id_tournament, id_phase):
        query = "INSERT INTO tournaments.match(id_tournament, id_phase) values({0},{1})".format(id_tournament, id_phase)
        self.con.execute(query)
        return True


