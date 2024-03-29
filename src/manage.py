from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_cors import CORS

import config
from models import db

server = Flask(__name__)
CORS(server, resources=r'/api/*')

server.debug = config.DEBUG
server.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URI
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(server)

migrate = Migrate(server, db)
manager = Manager(server)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()
