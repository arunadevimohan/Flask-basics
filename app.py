from flask import Flask, session, request, redirect, url_for, render_template
import secrets


app = Flask(__name__)
app.secret_key = secrets.token_hex(8)

@app.route('/', methods =['GET','POST'])
def home():
    
        return render_template("welcome.html")

@app.route('/profile')
def profile():
    if "name" in session: 
        user = {
            "name"  : session.get("name"),
            "age"   : session.get("age"),
            "city"  : session.get("city")
               }
        
        return render_template('profile.html', user = user)
    
    
    return redirect (url_for("login"))

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == "POST":
        name = request.values.get("name")
        age  = request.values.get("age")
        city = request.values.get("city")

        session['name'] = name
        session['age']  = age
        session['city'] = city
         
        print(f"session : {session}")
        return redirect(url_for("profile"))
    else:
        return render_template('login.html')

@app.route('/logout')
def session_logout():
    session.clear()
    return render_template("welcome.html")

if __name__ =='__main__':
    app.run(
        debug = True,
        port  = 6432
    )





    
    
