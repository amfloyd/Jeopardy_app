from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.templating import render_template
from flask_migrate import Migrate, migrate

app = Flask(__name__)
app.debug = True

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

#Create a SQLAlchemy instance
db = SQLAlchemy(app)

# Settings for migrations
migrate = Migrate(app, db)

#Tables
class scores(db.Model):
    user_name = db.Column(db.Integer, primary_key = True, nullable=False)
    high_score = db.Column(db.Integer, primary_key = False, default=0,\
    nullable = False)
    low_score = db.Column(db.Integer, primary_key = False, default=0,\
    nullable = False)
    attempts = db.Column(db.Integer, primary_key = False, default=0,\
    nullable = False)

    def __repr__(self):
        return f"Username : {self.user_name}, High Score: {self.high_score}\
         Low Score: {self.low_score}, Attempts: {self.attempts}"

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
