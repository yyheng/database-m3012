import hashlib

import mysql.connector as mysql

db = mysql.connect(
    host ="rm-gs595dd89hu8175hl6o.mysql.singapore.rds.aliyuncs.com",
    user ="ict1902698psk",
    passwd ="KSP8962091",
    database = "sql1902698psk"
)
cursor = db.cursor()

def UserAuth(cursor, Username, Password):
    query = "SELECT * FROM user WHERE user.UserName = '{0}' AND UserPw = SHA2('{1}',256)".format(Username,Password)
    #cursor = db.cursor(buffered=True)
    cursor.execute(query)
    result = cursor.fetchone()
    #Updating to check whether user have expired his paid priveledges
    # if (result[3] == 1):
    #     query = "SELECT * FROM order_details WHERE user.UserID = '{0}'".format(result[0])
    #     cursor.execute(query)
    #     receipt = cursor.fetchall()
    return result

def UserCreate(db, cursor, UserName, Password):
    query = "INSERT INTO user VALUES (%s, %s, SHA2(%s,256), DEFAULT(TierID), DEFAULT(isAdmin))"
    val = (0, UserName,Password)
    cursor.execute(query, val)
    db.commit()
    return True



print(UserAuth(cursor,"test","1234"))
# UserCreate(cursor,"anothertest","1234")
