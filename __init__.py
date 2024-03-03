from flask import Flask, render_template
from database_manager import DatabaseManager
from config import db_config

app = Flask(__name__)
db = DatabaseManager(db_config)


@app.route("/")
def home():
    # TODO: find the col size according to the number of data
    return render_template(
        "index.html",
        sectors=(sectors := db.get_sectors()),
        col_size=12 // len(sectors),
    )


@app.route("/get_resources/<sector_id>")
def get_resources(sector_id: int):
    return render_template(
        "resources.html",
        resources=(resources := [x for x in db.get_resources_by_sector(sector_id)]),
        col_size=12 // len(resources),
    )


@app.route("/resources/<resource_id>")
def resource(resource_id: int):
    return db.get_resource(resource_id)


if __name__ == "__main__":
    app.run(debug=True)
