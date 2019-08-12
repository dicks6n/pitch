from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Pitch, Comments
from flask_migrate import Migrate, MigrateCommand



# app = create_app('production')
app = create_app('production')

manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Pitch = Pitch, Comments= Comments)

@manager.command
def test():
    """
    """
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity = 2).run(tests)

if __name__ == '__main__':
    manager.run()