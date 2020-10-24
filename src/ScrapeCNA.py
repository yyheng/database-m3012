import requests
from bs4 import BeautifulSoup
from src.SentimentTest1 import SentimentAnalyse

def ScrapeCNA():
    contentlinks = []
    page = requests.get("https://www.channelnewsasia.com/action/news/8396414/search?q=Health&page=0", headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all("a", class_="teaser__title")
    for section in results:
        #print("Title is = " + section.get_text())
        #print("href is = " + section.get("href"))
        contentlinks.append(section.get("href"))

    for links in contentlinks:
        print("----------------------")
        print("https://www.channelnewsasia.com/" + links)
        #Find Author
        contentpage = requests.get("https://www.channelnewsasia.com/" + links)
        soup = BeautifulSoup(contentpage.content, 'html.parser')
        author_results = soup.find("a", class_="article__author-title")

        if (author_results != None):
            for string in author_results.stripped_strings:
                if string != "By":
                    print(repr(string))

        #Find Content
        content_result = soup.find("div", class_="c-rte--article")
        if content_result == None:
            continue
        content_result = content_result.findAll("p")
        x = 0
        for i in content_result:
            if i.find(class_='c-picture--article'):
                continue
            x += SentimentAnalyse(i.getText())
            print(i.getText())
        print(x)
        #Find Date
        Dateresult = soup.find("time", class_="article__details-item")
        print(Dateresult.getText())

ScrapeCNA()


