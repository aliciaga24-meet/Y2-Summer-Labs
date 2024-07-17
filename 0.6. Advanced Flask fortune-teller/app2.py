from flask import Flask, render_template
import random

app = Flask(__name__)

# Route for the home page
@app.route('/home')
def home():
    return render_template('home2.html')

@app.route('/fortune')
def fortune():
    fortunes = [
        "You will have a great day!",
        "A surprise is waiting for you.",
        "Today is your lucky day!",
        "Happiness will find you.",
        "Be cautious today.",
        "You will meet someone special.",
        "An opportunity will arise.",
        "Expect the unexpected.",
        "Good news is coming your way.",
        "You will achieve your goals."
    ]
    chosen_fortune = random.choice(fortunes)
    return render_template('fortune.html', fortune=chosen_fortune)

@app.route('/indecisive')
def indecisive():
    fortunes = [
        "You will have a great day!",
        "A surprise is waiting for you.",
        "Today is your lucky day!",
        "Happiness will find you.",
        "Be cautious today.",
        "You will meet someone special.",
        "An opportunity will arise.",
        "Expect the unexpected.",
        "Good news is coming your way.",
        "You will achieve your goals."
    ]
    chosen_fortunes = random.sample(fortunes, 3)
    return render_template('indecisive.html', fortunes=chosen_fortunes)

@app.route('/magic')
def magic():
    return render_template('magic.html')

@app.route('/response')
def response():
    responses = [
        "Yes",
        "No",
        "Maybe",
        "Only on Tuesdays",
        "I think so, but one can never be sure",
        "Why are you asking me?"
    ]
    chosen_response = random.choice(responses)
    return render_template('response.html', response=chosen_response)
# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)