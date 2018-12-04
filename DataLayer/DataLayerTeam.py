from DataLayer.Connection import Connection
from Entities.Team import Team


class DataLayerTeam:

    def __init__(self):
        self.con = Connection()

    def create_team(self, team):
        query = "INSERT INTO team(tournament_name) values({0})".format(repr(team.team_name))
        self.con.execute(query)
        id = self.con.cur.lastrowid
        return Team(id, team.team_name)

    def list_teams(self):
        teams = []
        query = "Select * From team"
        self.con.execute(query)
        t = self.con.cur.fetchall()
        for i in t:
            teams.append(i)
        return teams
