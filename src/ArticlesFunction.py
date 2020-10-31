import mysql.connector as mysql
from datetime import datetime
import hashlib

db = mysql.connect(
    host ="rm-gs595dd89hu8175hl6o.mysql.singapore.rds.aliyuncs.com",
    user ="ict1902698psk",
    passwd ="KSP8962091",
    database = "sql1902698psk"
)
cursor = db.cursor()

def SelectAllArticleTitle(cursor):
    query = "SELECT a.ArticleID, a.ArticleTitle, a.ArticleDate, c.CategoryName, p.AgencyName FROM article a, articlecategory c, agency p WHERE a.AgencyID = p.AgencyID AND a.CategoryID = c.CategoryID ORDER BY a.ArticleDate DESC"
    cursor.execute(query)
    results = cursor.fetchall()
    Homepageresults = []
    for result in results:
        article = (result[0],result[1],result[2].strftime("%d/%m/%Y"),result[3],result[4])
        Homepageresults.append(article)
    return Homepageresults

def SelectArticleDetails(cursor, articleID):
    #Title, Date, URL, Sentiment, ArticleText,CategoryName, Agency Name
    query = "SELECT a.ArticleTitle, a.ArticleDate,a.ArticleURL,a.SentimentRating,a.ArticleText, c.CategoryName, p.AgencyName FROM article a, articlecategory c, agency p WHERE a.AgencyID = p.AgencyID AND a.CategoryID = c.CategoryID AND ArticleID = {0}".format(articleID)
    cursor.execute(query)
    result = cursor.fetchone()
    listresult = list(result)
    listresult[1] = listresult[1].strftime("%d/%m/%Y")
    return listresult

print(SelectArticleDetails(cursor,2427))
#print(SelectAllArticleTitle(cursor)[0])