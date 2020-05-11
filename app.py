from flask import Flask, session, render_template, request
import pyrebase

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Leyno'

@app.errorhandler(403)
def error403(error):
    return '<h1> Notandi ekki til!</h1>', 403

@app.errorhandler(404)
def error404(error):
    return '<h1> Notandi ekki til!</h1>', 404

@app.errorhandler(405)
def error405(error):
    return '<h1> Notandi ekki til!</h1>', 405

@app.errorhandler(500)
def error500(error):
    return '<h1> Notandi ekki til!</h1>', 500

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

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            nafn = request.form['notendanafn']
            lykilord = request.form['lykilord']
            u = db.child("user").get().val()
            lst = list(u.items())
            talaID= 0
            teljari= len(lst)
            for i in lst:
                print(i)
                ID = i[1]['usr']
                PWD = i[1]['pwd']
                if nafn == ID and lykilord == PWD:
                    return render_template("User.html", ID = ID, PWD = PWD)
                if nafn == ID and lykilord != PWD:
                    return '<h1>Vitlaust lykilorð!</h1>'
                if nafn != ID:
                    talaID = talaID + 1
                    print(talaID)
                    print(teljari)
                if talaID == teljari:
                    return '<h1>Notandi ekki til</h1>'

    except:
        return "<h1>Notandi ekki til. Reyndu aftur!</h1>"
    return render_template("home.html")

@app.route('/register')
def register():
    return render_template("register.html")

account = []
@app.route('/info', methods=['GET', 'POST'])
def info():
    print(account)
    if request.method == 'POST':
        notendanafn = request.form['notendanafn']
        lykilord = request.form['lykilord']
        if notendanafn in account:
            return "<h1>Notandanafn tekin. Veldu annað!</h1>"
        db.child("user").push({"usr":notendanafn, "pwd":lykilord})
        nam=notendanafn
        account.append(nam) 
        return '<h1>Account created<h1> <br><a href="/">Return to homepage</a>'
    else:
        return "<h1>ma ekki </h1>"

"""
@app.route('/lesa')
def lesa():
    u = db.child("user").get().val()
    lst = list(u.items())
    tala=0
    for x in lst:
        print(lst[tala][1]['usr'])
        tala = tala + 1
    print(lst[0][1]['usr'])
    print(lst[1][1]['usr'])
    return "Lesum úr grunni"
"""
if __name__ == "__main__":
	app.run(debug=True)
