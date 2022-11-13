from app import app
from app.db import db

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    with app.app_context():
        db.create_all()
    app.run(port=5000,debug=True)