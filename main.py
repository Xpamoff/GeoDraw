from flask import Flask, request, render_template, session, redirect
from flask_sqlalchemy import SQLAlchemy
import compare
import random

app = Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///geodraw.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
#
#
# class Country(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(240), nullable=False)
#     path = db.Column(db.String(240), nullable=False)
#     region = db.Column(db.String(240), nullable=False)

country = [["Russia", "countries/russia.jpg", "Europe / Asia"],
           ["Germany", "countries/russia.jpg", "Europe"],
           ["New Zealand", "countries/russia.jpg", "Oceania"],
           ["Egypt", "countries/russia.jpg", "Africa"],
           ["United States", "countries/russia.jpg", "North America"]]


@app.route('/')
def index():
    number = random.randint(0, 4)
    draw_country = country[number]
    session['draw_country'] = draw_country
    return render_template('index.html', country=draw_country[0])

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/compare', methods=['GET', 'POST'])
def result():
    if request.method == "POST" and session.get('draw_country', None):
        url = request.form.get('url')
        draw_country = session.get('draw_country', None)
        hash1, hash2, compared = compare.compare(url, draw_country[1])
        return render_template('compare.html',
                               hash1=hash1,
                               hash2=hash2,
                               compared=compared,
                               country=draw_country[0],
                               path=draw_country[1],
                               region=draw_country[2],
                               original=url)
    else:
        return redirect('/')


if __name__ == '__main__':
    app.secret_key = 'ThOD4fSYjEDhma9YgIq33NIcgSJhqxDA4hHTPqlDzXY'
    app.run(debug=True)
