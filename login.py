from flask import Flask, request, render_template, jsonify, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("login.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    if(email=='rudra@mail.com' and password=='Pass@1234'):
        return f"Logged In Successfully"
    else:
        return f"Wrong credentials"    



@app.route('/signup')
def signup():
    return render_template('signup.html')












if __name__ == '__main__':
    app.run(debug=True)