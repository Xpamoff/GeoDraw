from flask import Flask, request, render_template, session, redirect
from flask_sqlalchemy import SQLAlchemy
import compare

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///geodraw.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(240), nullable=False)
    path = db.Column(db.String(240), nullable=False)
    region = db.Column(db.String(240), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/compare', methods=['GET', 'POST'])
def result():
    if request.method == "POST":
        url = request.form.get('url')
        hash1, hash2, compared = compare.compare(url)
        return render_template('compare.html', hash1=hash1, hash2=hash2, compared=compared)
    else:
        return redirect('/')


if __name__ == '__main__':
    app.secret_key = 'grippingsecretkey'
    app.run(debug=True)
