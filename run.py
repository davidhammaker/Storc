import sys
from storc import create_app, db


app = create_app()


if __name__ == '__main__':
    if '--setup' in sys.argv:
        app.app_context().push()
        db.create_all()
    app.run(debug=True)
