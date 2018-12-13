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

    def result(self, match, score_team_1, score_team_2):
        query = "UPDATE tournaments.match set score_team_1 = {0}, score_team_2 = {1} WHERE id_match = {2}".format(score_team_1, score_team_2, match.id)
        self.con.execute(query)
        return self.get_match(match.id)

    def winner(self, match, team_winner):
        id_phase = int(match.id_phase / 2)
        if match.id_phase % 2 != 0:
            query = "UPDATE tournaments.match set team_1 = {0} WHERE id_tournament = {1} AND id_phase = {2}".format(team_winner, match.id_tournament, id_phase)
        else:
            query = "UPDATE tournaments.match set team_2 = {0} WHERE id_tournament = {1} AND id_phase = {2}".format(team_winner, match.id_tournament, id_phase)
        self.con.execute(query)
        return self.get_match(match.id)

    def get_matches(self, tournament, range_matches):
        matches = []
        query = "SELECT * FROM tournaments.match WHERE id_tournament = {0} AND id_phase >= {1} AND id_phase <= {2}".format(tournament.id, range_matches[0], range_matches[1])
        self.con.execute(query)
        t = self.con.cur.fetchall()
        for i in t:
            matches.append(Match(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
        return matches

    def get_match(self, id):
        query = "SELECT * FROM tournaments.match where id_match = {0}".format(id)
        self.con.execute(query)
        s = self.con.cur.fetchone()
        return Match(s[0], s[1], s[2], s[3], s[4], s[5], s[6])

    def is_match_done(self, id, id_phase):
        print(id)
        query = "SELECT * FROM tournaments.match where id_tournament = {0} AND id_phase = {1}".format(id, id_phase)
        self.con.execute(query)
        s = self.con.cur.fetchone()
        print(s[0], s[1], s[2])
        if s[5] is not None and s[6] is not None:
            return True
        return False

    def create_next_match(self, id_tournament, id_phase):
        query = "INSERT INTO tournaments.match(id_tournament, id_phase) values({0},{1})".format(id_tournament, id_phase)
        self.con.execute(query)
        return True

    def get_finals(self):
        query = "SELECT * FROM tournaments.match WHERE id_phase = 1"
        self.con.execute(query)
        finals = self.con.cur.fetchall()
        return finals
