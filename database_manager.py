import psycopg2


class DatabaseManager:
    def __init__(self, config: dict[str, any]):
        self.conn = psycopg2.connect(
            dbname=config["dbname"],
            user=config["user"],
            password=config["password"],
            host=config["host"],
            port=config["port"],
        )
        self.cur = self.conn.cursor()

    def get_sectors(self):
        self.cur.execute("select * from get_sectors();")
        return self.cur.fetchall()

    def get_resources_by_sector(self, sector_id: int):
        self.cur.execute(f"select * from get_resources_in_sector({sector_id});")
        return self.convert_into_dict()

    def get_resource(self, resource_id: int):
        self.cur.execute(f"select * from resources where id={resource_id};")
        return self.convert_into_dict()

    def convert_into_dict(self):
        # TODO: this should be a decorator
        table_cols = [desc[0] for desc in self.cur.description]
        data = self.cur.fetchall()
        return [dict(zip(table_cols, row)) for row in data]


if __name__ == "__main__":
    from config import db_config as config

    db = DatabaseManager(config)
    print(db.get_sectors())
    print(db.get_resources_by_sector(1))
