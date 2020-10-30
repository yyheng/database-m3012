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
    query = "SELECT * FROM user WHERE user.UserName = '{0}' AND UserPw = MD5('{1}')".format(Username,Password)
    cursor.execute(query)
    result = cursor.fetchone()
    return result

def UserCreate(db, cursor, UserName, Password):
    query = "INSERT INTO user VALUES (%s, %s, MD5(%s), DEFAULT(TierID), DEFAULT(isAdmin))"
    val = (0, UserName,Password)
    cursor.execute(query, val)
    db.commit()
    return True


#print(UserAuth(cursor,"test","123"))
# UserCreate(cursor,"anothertest","1234")
