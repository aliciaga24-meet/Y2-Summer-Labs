from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        birth_month = request.form['birth_month']
        session['name'] = name
        session['birth_month'] = birth_month
        
        return render_template('home2.html' ,  name = name)
    return render_template('login.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'name' not in session:
        return redirect(url_for('login'))
    return render_template('home2.html')

@app.route('/fortune')
def fortune():
    fortunes = [
        "You will find money!",
        "What doesn't kill you makes you stronger.",
        "L L L",
        "Be happy.",
        "Work hard.",
        "Be who you are.",
        "Live love.",
        "Yippiee!",
        "Love is in the air."
    ]

    index = len(session["birth_month"]) % len(fortunes) 
    fortune = fortunes[index]

    return render_template('fortune.html', fortune=fortune)

if __name__ == '__main__':
    app.run(debug=True)
