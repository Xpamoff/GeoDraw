from flask import Flask, request, render_template, session, redirect
from flask_sqlalchemy import SQLAlchemy
import compare
import random

app = Flask(__name__)


country = [["Russia", "countries/russia.jpg", "Europe / Asia"],
           ["Germany", "countries/russia.jpg", "Europe"],
           ["New Zealand", "countries/russia.jpg", "Oceania"],
           ["Egypt", "countries/russia.jpg", "Africa"],
           ["United States", "countries/russia.jpg", "North America"]]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/draw', methods=['GET', 'POST'])
def draw():
    if request.method == "POST":
        region = request.form.get('region')
        if region == "Europe":
            while True:
                number = random.randint(0, 4)
                if "Europe" in country[number][2]:
                    break
        else:
            number = random.randint(0, 4)
    else: 
        return redirect('/')
    draw_country = country[number]
    session['draw_country'] = draw_country
    return render_template('draw.html', country=draw_country[0])

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
