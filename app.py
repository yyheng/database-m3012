from flask import Flask, redirect, url_for, render_template

app = Flask(
    __name__, 
    template_folder="templates",
    )


#return route to index view
@app.route("/")
def index():
    #return redirect(url_for("index"))
    return render_template("main/index.htm")


#return route to login view
@app.route("/login")
def login():
    return render_template("main/login.htm")

#return route to register view
@app.route("/register")
def register():
    return render_template("main/register.htm")

#run application
if __name__ == '__main__':
    app.run(debug = True)