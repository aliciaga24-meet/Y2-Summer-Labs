from flask import Flask, render_template ,request, redirect, url_for 
from flask import session
import pyrebase

app = Flask(__name__,
    template_folder ="templates",
    static_folder='static')
app.config["SECRET_KEY"] = "MMM"

firebaseConfig = {
  "apiKey": "AIzaSyC4GqtuykzB4GNbMnmaUgXquJXuSB_DUm8",
  "authDomain": "auth-lab-aea23.firebaseapp.com",
  "projectId": "auth-lab-aea23",
  "storageBucket": "auth-lab-aea23.appspot.com",
  "messagingSenderId": "628390945462",
  "appId": "1:628390945462:web:7cc39f472828cd1e73fc17",
  "databaseURL":"https://auth-lab-aea23-default-rtdb.europe-west1.firebasedatabase.app/"

}

firebase = pyrebase.initialize_app(firebaseConfig) 
auth = firebase.auth()
db =firebase.database()


@app.route('/', methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html") 
    
    email = request.form['email']
    password = request.form['password']
    full_name = request.form['full_name']
    username = request.form['username']
    #try:
    session['user'] = auth.create_user_with_email_and_password(email, password)
    user = {

    'email': email,
    'password': password,
    'full_name': full_name,
    'username': username
    }
    db.child("Users").child(session['user']['localId']).set(user)
    return redirect(url_for('home'))
    #except:
    #    error_msg = "Womp it failed. Try again"
    #    return render_template("signup.html",error=error_msg)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        return render_template("signin.html") 
    
    email = request.form['email']
    password = request.form['password']
    try:
        session['user'] = auth.sign_in_with_email_and_password(email, password)
        session["quotes"] = []
        return redirect(url_for('home'))
    except:
        error_msg = "Womp it failed sad"
        return render_template("signin.html", error=error_msg)


@app.route('/home', methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    quote = request.form['quote']
    author = request.form['']
    quotes = {
        'text':quote ,
        'said_by_who': author,
        'uid': session['user']["localId"]
    }
    db.child("quotes").push(quotes)
    return redirect(url_for('thanks')) 
  return render_template('home.html')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/display')
def display():
  return render_template('display.html',massage = db.child("quotes").get().val())

def signout():
    session["user"] = None
    return redirect(url_for('signin'))

if __name__ == '__main__':
    app.run(debug=True)