from flask import Flask, redirect, url_for, render_template, request, flash, session
from flask_login import login_user, login_required, current_user
import mysql.connector as mysql

from src.UserFunctions import UserAuth

#UserName: test PW:123 Admin

app = Flask(
    __name__, 
    template_folder="templates",
    )
app.secret_key = "super secret key"

db = mysql.connect(
    host ="rm-gs595dd89hu8175hl6o.mysql.singapore.rds.aliyuncs.com",
    user ="ict1902698psk",
    passwd ="KSP8962091",
    database = "sql1902698psk"
)
cursor = db.cursor()

########################### MAIN ###########################
#return route to index view
@app.route("/")
def article():
    #return redirect(url_for("index"))
    return render_template("main/article.htm")

#return route to login view
@app.route("/login")
def login():
        return render_template("main/login.htm")

#login route input view
@app.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('usernameTB')
    password = request.form.get('passwordTB')

    # flash(username)
    # return redirect(url_for('login'))

    if not UserAuth(cursor, username, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('login'))
    login_user(username)
    return redirect(url_for('user_article'))
        

#return route to register view
@app.route("/register")
def register():
    return render_template("main/register.htm")

########################### USER ###########################
#return route to user dashboard view
@app.route("/user_dashboard")
def user_dashboard():
    return render_template("main/user_dashboard.htm")


#return route to user article view
@app.route("/user_article")
@login_required
def user_article():
    return render_template("main/user_article.htm")

#return route to user favourite view, profile, privillege, etc
@app.route("/user_profile")
def user_profile():
    return render_template("main/user_profile.htm")

#return route to user purchase view
@app.route("/user_purchase")
def user_purchase():
    return render_template("main/user_purchase.htm")

#return route to user purchase view
@app.route("/user_privilege")
def user_privilege():
    return render_template("main/user_privilege.htm")

####################### ADMINISTRATOR #######################
#return route to admin dashboard view
@app.route("/admin_dashboard")
def admin_dashboard():
    return render_template("main/admin_dashboard.htm")

#run application
if __name__ == '__main__':
    app.run(debug = True)