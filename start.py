from pic_pro.views import app
from pic_pro.extension import db
from flask import current_app

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    print ('\n ',app.view_functions)
    app.run(debug=True)