import pymysql


class Connection:
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host='127.0.0.1',
                user='root',
                password='root',
                db='tournaments')
            self.cur = self.conn.cursor()
        except Exception as f:
            print("Error al ejecutar SQL " + str(f))

    def execute(self, query):
        self.cur.execute(query)
        self.conn.commit()


if __name__ == '__main__':
    con = Connection()


