from flask import Flask, session, request, redirect, url_for, render_template
import secrets







app = Flask(__name__)
app.secret_key = secrets.token_hex(8)

users = {
            "aruna"  : "Sivagangai",
            "steve"  : "Coimbatore"
            }


@app.route('/', methods =['GET','POST'])
def home():
    
        return render_template("welcome.html")

@app.route('/profile')
def profile(): 
    if "user_name" in session :
       
        user_name = session.get("user_name")
        if user_name in users:
            users={
                "name" :user_name, 
                "city"  : users[user_name]
            }
        return render_template('profile.html', user_name = users )
    return redirect (url_for("login"))
       

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == "POST":
        user_name = request.values.get("user_name")
        if user_name in users:

            session['name'] = user_name
        
         
            print(f"session : {session}")
            return redirect(url_for("profile"))
        else:
            error = "invalid user_name"
               
    return render_template('login.html', error= error)

@app.route('/logout')
def session_logout():
    session.clear()
    return render_template("welcome.html")

if __name__ =='__main__':
    app.run(
        debug = True,
        port  = 6432
    )





    
    
