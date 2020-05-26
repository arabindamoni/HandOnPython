from flask import Flask, render_template, request

app = Flask(__name__)

# this method returns True if username and password combination is correct else returns False
def authenticate(username, password):
    return False


@app.route("/login", methods=["post"])
def login():
    if request.method == 'POST': 
        username, password = request.form["username"], request.form["password"]
        if authenticate(username,password):
            message = f"welcome {username}"
        else:
            message = f"Logid failed: username/password incorrect"
        return render_template("message.html", message = message, success=False)
    else:
        return "only post requests are allowed"


@app.route('/')
def home():    
    return render_template("index.html")    

if __name__ == '__main__':
    app.run()