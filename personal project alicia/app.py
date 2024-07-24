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

animal1 = { "type": "cat", "name" : "kitty", "age": "1","place": "russia"}
animal2 = { "type": "dog", "name" : "halo", "age": "2","place": "israel"}
animal3 = { "type": "rabbit", "name" : "dan", "age": "7","place": "israel"}
animal5 = { "type": "dog", "name" : "abdalla", "age": "4","place": "israel"}
animal6 = { "type": "cat", "name" : "bae", "age": "52","place": "israel"}
animal7 = { "type": "rabbit", "name" : "pookie", "age": "10","place": "russia"}
animal8 = { "type": "cat", "name" : "cookie", "age": "4","place": "russia"}
animal9 = { "type": "cat", "name" : "banana", "age": "99","place": "russia"}

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

    db.child("animals").push(animal1)
    db.child("animals").push(animal2)
    db.child("animals").push(animal3)
    db.child("animals").push(animal5)
    db.child("animals").push(animal6)
    db.child("animals").push(animal7)
    db.child("animals").push(animal8)
    db.child("animals").push(animal9)
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
    if 'user' in session and session['user'] and 'localId' in session['user']:
      pets = request.form['pets']
      place = request.form['place']
      preferences = {
        'pet_type': pets,
        'place': place
      }

      try:
        db.child("Users").child(session['user']["localId"]).child("preferences").set(preferences)
        return redirect(url_for('home'))
      except Exception as e:
        print(f"Error saving preferences: {e}")
        return render_template('error.html', message='Error saving preferences')

    else:
      return redirect(url_for('signin'))
  return render_template('save_prefrence.html')

@app.route('/signout')
def signout():
    session["user"] = None
    return redirect(url_for('opening'))

@app.route('/home', methods=['POST', 'GET'])
def home():
  animal = db.child('animals').get().val()
  prefer = db.child("Users").child(session['user']["localId"]).child("preferences").get().val()
  animals = []
  places = []

  for id, i in animal.items():    
      if prefer['pet_type'] == i['type'] and prefer['place'] == i['place']:
        animals.append({"animal":i, "id":id})
        places.append({"animal":i, "id":id})
  if request.method == "POST":
    if request.args.get("id") is not None:
      id = request.args.get("id")
      session["animal_adopted"] = db.child("animals").child(id).get().val()
      db.child("animals").child(id).remove()
      return redirect(url_for("adopt"))
    else:
      name = request.form["name"]
      age = int(request.form["age"])
      place = request.form['place']
      pets = request.form["pets"]
      db.child("animals").push({
        "name": name,
        "age": age,
        "place": place,
        "type": pets
        })

  return render_template('home.html',animal=animals)

@app.route('/adopt', methods=['POST','GET'])
def adopt():
  if request.method == "GET":
      return render_template("adopted.html", animal=session["animal_adopted"])


if __name__ == '__main__':
  app.run(debug=True)