from DataLayer.Connection import Connection
from Entities.Tournament import Tournament
from Entities.Match import Match


class DataLayerMatch:

    def __init__(self):
        self.con = Connection()

    def create_match(self, team_1, team_2, id_tournament, id_phase):
        query = "INSERT INTO tournaments.match(team_1, team_2, id_tournament, id_phase) values({0},{1},{2},{3})".format(team_1, team_2, id_tournament, id_phase)
        self.con.execute(query)
        return True

    def get_matches(self, tournament, range_matches):
        print(tournament.id, range_matches)
        matches = []
        query = "SELECT * FROM tournaments.match WHERE id_tournament = {0} AND id_phase >= {1} AND id_phase <= {2}".format(tournament.id, range_matches[0], range_matches[1])
        self.con.execute(query)
        t = self.con.cur.fetchall()
        for i in t:
            matches.append(Match(i[0], i[1], i[2], i[3], i[4], i[5]))
        return matches

    def create_next_match(self, id_tournament, id_phase):
        query = "INSERT INTO tournaments.match(id_tournament, id_phase) values({0},{1})".format(id_tournament, id_phase)
        self.con.execute(query)
        return True


