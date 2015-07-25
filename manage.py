from app import create_app, db
from app.models import CoffeeShop
from flask.ext.script import Manager, Shell

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db, CoffeeShop=CoffeeShop)
    manager.add_command("shell", Shell(make_context=make_shell_context))

f __name__ == '__main__':
    manager.run()
