from flask import Flask, request, render_template, redirect, url_for
import random

app = Flask(__name__)


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        birth_month = request.form['birth_month']
        return redirect(url_for('fortune', birth_month=birth_month))
    
    return render_template('home2.html')


@app.route('/fortune/<string:birth_month>')
def fortune(birth_month):
    fortunes = [
        "you will find money!",
        "what doesnt kill you makes you stronger.",
        "L L L",
        "be happy.",
        "work hard.",
        "be who you are.",
        "live love lught",
        "Adventure awaits you this month.",
        "yippiee ",
        "Love is in the air."
    ]

    index = len(birth_month) % len(fortunes) 
    fortune = fortunes[index]

    return render_template('home2.html', fortune=fortune)



if __name__ == '__main__':
    app.run(debug=True)