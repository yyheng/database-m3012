import mysql.connector as mysql
from datetime import datetime
import hashlib

# db = mysql.connect(
#     host ="rm-gs595dd89hu8175hl6o.mysql.singapore.rds.aliyuncs.com",
#     user ="ict1902698psk",
#     passwd ="KSP8962091",
#     database = "sql1902698psk"
# )
# cursor = db.cursor()

def SelectAllArticleTitle(cursor):
    query = "SELECT a.ArticleTitle, a.ArticleDate, c.CategoryName, p.AgencyName FROM article a, articlecategory c, agency p WHERE a.AgencyID = p.AgencyID AND a.CategoryID = c.CategoryID ORDER BY a.ArticleDate DESC"
    cursor.execute(query)
    results = cursor.fetchall()
    Homepageresults = []
    for result in results:
        article = (result[0],result[1].strftime("%d/%m/%Y"),result[2],result[3])
        Homepageresults.append(article)
    return Homepageresults

#print(SelectAllArticleTitle(cursor)[0])