from flask import Flask, session, render_template, request
import pyrebase

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Leyno'

@app.errorhandler(404)
def error404(error):
    return '<h1> Síða ekki til!</h1>', 404

config = {
    "apiKey": "AIzaSyCjVuTataPfXP1TFX7g4sjFPth6_9gGFV0",
    "authDomain": "verkefni5-2020.firebaseapp.com",
    "databaseURL": "https://verkefni5-2020.firebaseio.com",
    "projectId": "verkefni5-2020",
    "storageBucket": "verkefni5-2020.appspot.com",
    "messagingSenderId": "275636380925",
    "appId": "1:275636380925:web:89e1a26445951ad8120a94",
    "measurementId": "G-GBT4MMGQFQ"
}

fb = pyrebase.initialize_app(config)
db = fb.database()


@app.route('/')
def index():
    return render_template("home.html")

@app.route('/Logged/<id>', methods=['GET', 'POST'])
def Logged(id):
    return render_template("Login.html")

@app.route('/info', methods=['GET', 'POST'])
def info():
    if request.method == 'POST':
        notendanafn = request.form['notendanafn']
        lykilord = request.form['lykilord']
        db.child("user").push({"usr":notendanafn, "pwd":lykilord}) 
        return '<a href="/">Login page</a>'
    else:
        return "<h1>ma ekki </h1>"

@app.route('/register')
def register():
    return render_template("register.html")

"""
@app.route('/lesa')
def lesa():
    u = db.child("user").get().val()
    lst = list(u.items())
    tala=len(lst)
    account=[]
    for x in range(tala-1):
        account.append(lst[x])
    print(lst[0][0]['pwd'])
    print(lst[0][1]['usr'])
    return "Lesum úr grunni"
"""
if __name__ == "__main__":
	app.run(debug=True)
