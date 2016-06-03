from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
# from flask_sqlalchemy import SQLAlchemy

from pydojo import create_app, db
from pydojo.config import BaseConfig

app = create_app(BaseConfig)
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
