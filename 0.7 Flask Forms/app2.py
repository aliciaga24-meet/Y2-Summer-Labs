from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home2.html')

@app.route('/fortune')
def fortune():
    fortunes = [
        "You will have a great day!",
        "the day will come",
        "you'll find money on the floor today"
    ]
    chosen_fortune = random.choice(fortunes)
    return render_template('fortune.html', fortune=chosen_fortune)

if __name__ == '__main__':
    app.run(debug=True)