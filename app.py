from flask import Flask, session, request, redirect, url_for, render_template
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(8)

users = {
    "aruna"  : "Sivagangai",
    "steve"  :  "Coimbatore"
}


@app.route('/')
def home():
    return render_template("welcome.html")

@app.route('/profile')
def profile(): 
    if "username" in session :
        username = session.get("username")
        if username in user:
            user ={
                "name" :username, 
                "city"  : users[username]
            }
            return render_template('profile.html', username=user )
        
        
        return render_template('profile.html')
   
    return redirect (url_for("login"))
       

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == "POST":
        username = request.values.get("username")
        print(f"username:{username}")
        if username in users:
            session['username'] = username
            print(f"session : {session}")
            return redirect(url_for("profile"))
        else:
            return "invalid username"
    return render_template('login.html')
        #else:
            #return "invalid user_name"
        

@app.route('/logout')
def session_logout():
    session.clear()
    return render_template("welcome.html")

if __name__ =='__main__':
    app.run(
        debug = True,
        port  = 6432
    )





    
    
