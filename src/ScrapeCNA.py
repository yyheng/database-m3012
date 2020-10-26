import requests
from bs4 import BeautifulSoup
from src.SentimentTest1 import SentimentAnalyse
from datetime import datetime
import random
import mysql.connector as mysql

def ScrapeCNA(category):
    #1 is health, #2 is business, #3 politics
    if category == 1:
        search = "health"
    elif category == 2:
        search = "business"
    else:
        search = "politics"
    db = mysql.connect(
        host="rm-gs595dd89hu8175hl6o.mysql.singapore.rds.aliyuncs.com",
        user="ict1902698psk",
        passwd="KSP8962091",
        database="sql1902698psk"
    )
    cursor = db.cursor()
    contentlinks = []
    user_agent_list = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    ]
    for i in range(5):
        user_agent = random.choice(user_agent_list)
        page = requests.get("https://www.channelnewsasia.com/action/news/8396414/search?q={0}&page={1}".format(search,i), headers={'User-Agent': user_agent})
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find_all("a", class_="teaser__title")
        for section in results:
            #print("Title is = " + section.get_text())
            #print("href is = " + section.get("href"))
            contentlinks.append(section.get("href"))

        for links in contentlinks:
            SentimentRating = 0
            ArticleText = ""
            AuthorID = None
            AgencyID = 2
            CategoryID = category
            print("----------------------")
            print("https://www.channelnewsasia.com/" + links)
            ArticleURL = "https://www.channelnewsasia.com/" + links
            #Find Author
            contentpage = requests.get("https://www.channelnewsasia.com/" + links)
            soup = BeautifulSoup(contentpage.content, 'html.parser')
            author_results = soup.find("a", class_="article__author-title")

            if (author_results != None):
                for string in author_results.stripped_strings:
                    if string != "By":
                        print(repr(string))

            #Find Title
            Title = soup.find("h1", class_="article__title")
            if(Title != None):
                ArticleTitle = Title.getText()
            #Find Content
            content_result = soup.find("div", class_="c-rte--article")
            if content_result == None:
                print("No results")
                continue
            content_result = content_result.findAll("p")
            for i in content_result:
                if i.find(class_='c-picture--article'):
                    print("here")
                    continue
                SentimentRating += SentimentAnalyse(i.getText())
                ArticleText += i.getText()
                print(i.getText())
            #Find Date
            Dateresult = soup.find("time", class_="article__details-item")
            datetime_object = datetime.strptime(Dateresult.getText(), '%d %b  %Y %I:%M%p')
            ArticleDate = datetime_object.strftime("%Y-%m-%d")
            query = "INSERT INTO article VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (0,ArticleURL,ArticleTitle,ArticleDate,SentimentRating,ArticleText,"2",AgencyID,CategoryID)
            cursor.execute(query, val)
            print(ArticleDate)
            print(ArticleText)
            print(ArticleURL)
            print(SentimentRating)
            print(ArticleTitle)
    db.commit()

ScrapeCNA(3)


