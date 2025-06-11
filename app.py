from flask import Flask, render_template, request, url_for
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/letnji-kurs')
def letnji_kurs():
    return render_template('letnji-kurs.html')

@app.route('/prijava', methods=['POST'])
def prijava():
    ime = request.form['ime']
    razred = request.form['razred']
    email = request.form['email']
    telefon = request.form.get('telefon', '')

    with open('prijave.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([ime, razred, email, telefon])

    return render_template('hvala.html', ime=ime)

if __name__ == '__main__':
  import os
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)

