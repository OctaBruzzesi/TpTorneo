from DataLayer.Connection import Connection
from Entities.Team import Team


class DataLayerTeam:

    def __init__(self):
        self.con = Connection()

    def create_team(self, team):
        query = "INSERT INTO team(team_name) values({0})".format(repr(team.team_name))
        self.con.execute(query)
        id = self.con.cur.lastrowid
        return Team(id, team.team_name)

    def list_teams(self):
        teams = []
        query = "Select * From team WHERE habilitado = 1"
        self.con.execute(query)
        t = self.con.cur.fetchall()
        for i in t:
            teams.append(Team(i[0], i[1]))
        return teams

    def update_team(self, team):
        query = "UPDATE team set team_name = {0} WHERE id_team= {1}".format(repr(team.team_name), team.id)
        self.con.execute(query)
        return team

    def get_team(self, id):
        query = "SELECT * FROM team where id_team = {0} AND habilitado = 1".format(id)
        self.con.execute(query)
        t = self.con.cur.fetchone()
        team = Team(t[0],t[1])
        return team

    def delete_team(self, id):
        query = "UPDATE team SET habilitado = 0 WHERE id_team = {0}".format(id)
        self.con.execute(query)

    def search_byName(self, name):
        query = "SELECT * FROM team WHERE team_name = '{0}' AND habilitado = 1".format(name)
        self.con.execute(query)
        t = self.con.cur.fetchone()
        if t == None:
            return False
        else:
            return True
