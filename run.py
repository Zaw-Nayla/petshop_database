from db import db , app

db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()