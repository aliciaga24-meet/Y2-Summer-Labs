from flask import Flask, render_template ,request, redirect, url_for 
from flask import session
import pyrebase

app = Flask(__name__,
  template_folder ="templates",
  static_folder='static')
app.config["SECRET_KEY"] = "MMMlanscjjnclakjcnwjainc"

firebaseConfig = {
  "apiKey": "AIzaSyCoJsD22PcbjJ9FsF99iTrwlIHHkrfAeWk",
  "authDomain": "personal-project-9c6d4.firebaseapp.com",
  "databaseURL": "https://personal-project-9c6d4-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "personal-project-9c6d4",
  "storageBucket": "personal-project-9c6d4.appspot.com",
  "messagingSenderId": "541675344390",
  "appId": "1:541675344390:web:a66448b965df636cb26987"
}

firebase = pyrebase.initialize_app(firebaseConfig) 
auth = firebase.auth()
db =firebase.database()


@app.route('/', methods=['GET','POST'])
def opening():
  if request.method == 'GET':
        return render_template("opening.html") 
  return redirect(url_for('signup'))

@app.route('/signup', methods=['GET','POST'])
def signup():
  if request.method == 'POST':     
    email = request.form['email']
    password = request.form['password']
    user = auth.create_user_with_email_and_password(email, password)
    uid = user['localId']
    info = {
    'email': email,
    'password': password,
    'uid':uid
    }

    session['user'] = user
    
    db.child("Users").child(uid).set(info)
    return redirect(url_for('save_preferences'))
  else:
    print("went through else")
    return render_template("signup.html")

    
@app.route('/signin', methods=['GET', 'POST'])
def signin():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    user = auth.sign_in_with_email_and_password(email,password)
    session['user'] = user
    return redirect(url_for('save_preferences'))
  else:
    return render_template('signin.html')

@app.route('/save_preferences', methods=['POST', 'GET'])
def save_preferences():
    if request.method == 'POST':
      if 'user' in session:
        pets = request.form['pets']
        age = request.form['age']
        place = request.form['place']       
        preferences = {
            'pet_type': pets,
            'age': age,
            'place': place
        }        
        db.child("Users").child(session['user']["localId"]).child("preferences").set(preferences)
        return redirect(url_for('home'))
      else:
        return redirect(url_for('signin'))
    return render_template('save_prefrence.html')

@app.route('/signout')
def signout():
    session["user"] = None
    return redirect(url_for('opening'))

@app.route('/home', methods=['POST', 'GET'])
def home():
  animal = db.child('animals').get().val().values()
  if request == 'POST':
    prefer = db.child("Users").child(session['user']["localId"]).child("preferences").get().val()
    preferred_location = preferences.get('place')
  return render_template('home.html',animal=animal)

if __name__ == '__main__':
  app.run(debug=True)