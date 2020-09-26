from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Local Database Connection
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Before@123@localhost/quotes'

# Heroku Database Connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ogmgrphfxwsaoq:dcf9305713b5c60ae0b6d376960c64081d8f19dd6e9f104e3c3dc1c076470c8c@ec2-54-228-209-117.eu-west-1.compute.amazonaws.com:5432/d30d0q7bpe2mvt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Favqoutes(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))

@app.route('/')
def index():
    result = Favqoutes.query.all()
    return render_template('index.html', result = result)


@app.route('/quotes')
def quotes():
    return render_template('quotes.html')


@app.route('/process', methods=['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quoteData = Favqoutes(author = author, quote = quote)
    db.session.add(quoteData)
    db.session.commit()

    return redirect(url_for('index'))