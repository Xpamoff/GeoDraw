from flask import Flask, request, render_template, session
import compare

app = Flask(__name__)

actual_data = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/compare', methods=['GET', 'POST'])
def result():
    url = request.form.get('url')
    hash1, hash2, compared = compare.compare(url)
    return render_template('compare.html', hash1=hash1, hash2=hash2, compared=compared)


if __name__ == '__main__':
    app.secret_key = 'grippingsecretkey'
    app.run(debug=True)
