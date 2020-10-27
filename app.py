from flask import Flask, redirect, url_for, render_template
from flask_mysqldb import MySQL

app = Flask(
    __name__, 
    template_folder="templates",
    )

# configure database connection here using flask_mysqldb instead
app.config['MYSQL_HOST'] = "rm-gs595dd89hu8175hl6o.mysql.singapore.rds.aliyuncs.com"
app.config['MYSQL_USER'] = "ict1902698psk"
app.config['MYSQL_PASSWORD'] = "KSP8962091"
app.config['MYSQL_DB'] = "sql1902698psk"

mysql = MySQL(app)

########################### MAIN ###########################
#return route to index view
@app.route("/")
def article():
    #return redirect(url_for("index"))
    return render_template("main/article.htm")

#return route to login view
@app.route("/login")
def login():
    cur = mysql.connection.cursor()
    user = cur.execute("SELECT * FROM user")

    if user > 0:
        userInfo = cur.fetchall()
        
        return render_template("main/login.htm", userInfo=userInfo)

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