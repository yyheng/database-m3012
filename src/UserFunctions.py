import mysql.connector as mysql
import hashlib

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
    try:
        query = "INSERT INTO user VALUES (%s, %s, SHA2(%s,256), DEFAULT(TierID), DEFAULT(isAdmin),DEFAULT,DEFAULT)"
        val = (0, UserName,Password)
        cursor.execute(query, val)
        db.commit()
        return True
    except:
        return False

def InsertPaymentMethod(db, cursor, UserID, CardNo, CardExpiryDate):
    query = "UPDATE user SET CardNo = AES_ENCRYPT(%s,%s), CardExpiryDate = %s WHERE UserID = %s"
    val = (CardNo,UserID,CardExpiryDate,UserID)
    cursor.execute(query, val)
    db.commit()
    if cursor.rowcount > 0:
        return True
    else:
        return False


def SelectUserPayment(cursor, UserID):
    query = "SELECT CAST(AES_DECRYPT(CardNo,{0}) as CHAR),CardExpiryDate FROM user WHERE UserID = {0}".format(UserID)
    cursor.execute(query)
    result = cursor.fetchone()
    return result


#print(UserAuth(cursor,"test","123"))
#UserCreate(cursor,"anothertest","1234")

#print(InsertPaymentMethod(db,cursor,7,"5500 0000 0000 0004","03/21"))
#print (SelectUserPayment(cursor, 7))
#print(UserAuth(cursor,"test","1234"))
#UserCreate(db,cursor,"","1234")

