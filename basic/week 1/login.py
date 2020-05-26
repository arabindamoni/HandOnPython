from flask import Flask, render_template, request

app = Flask(__name__)

# this method returns True if username and password combination is correct else returns False
def authenticate(username, password):    

    # Attempt 4:
    # O(1)
    usernamedic = {
        "Shayani" : "1234",
        "Ria" : "dddd",
        "Arabinda":"abcd"
    }
    
    if username in usernamedic and usernamedic[username] == password:
        return True

    # usernameList = ["Shayani", "Arabinda", "Ria"]
    # passwordList = ["1234","abcd","dddd"]
    # Attempt 2:
    # O(n^2)
    # for x in usernameList:
    #     for y in passwordList:
    #         if username == x and password == y:
    #             return True
    
    # Attempt 3:
    # O(n)
    # for i in range(len(usernameList)):
    #     if username == usernameList[i] and password == passwordList[i]:
    #         return True  
    
    
    # Attempt 1: 
    # problem too much to write
    #if username == usernameList[0] and password == passwordList[0]:
        #return True
    #elif username == usernameList[1] and password == passwordList[1]:
        #return True      

    return False


@app.route("/login", methods=["post"])
def login():
    if request.method == 'POST': 
        username, password = request.form["username"], request.form["password"]
        success = authenticate(username,password)
        if success:
            message = f"welcome {username}"
        else:
            message = f"Logid failed: username/password incorrect"
        return render_template("message.html", message = message, success=success)
    else:
        return "only post requests are allowed"


@app.route('/')
def home():    
    return render_template("index.html")    

if __name__ == '__main__':
    app.run()