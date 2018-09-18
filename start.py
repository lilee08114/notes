from pic_pro.views import app
from pic_pro.extension import db
from flask import current_app
import os.path

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    print ('\n ',app.view_functions)
    print( os.path.abspath(os.path.dirname(__file__)))
    app.run(debug=True)