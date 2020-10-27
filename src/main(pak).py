import bs4 as bs
import urllib.request
import json
import re

class stArticle:
    def __init__(self, title, author, date, content, url):
        self.title = title
        self.author = author
        self.date = date
        self.content = content
        self.url = url

class todayArticle:
    def __init__(self, title, author, date, content, url):
        self.title = title
        self.author = author
        self.date = date
        self.content = content
        self.url = url

def stCrawl(url,pageCount):
    #number of pages
    stURLsList = []
    stArticlesList = []
    for pagenum in range(pageCount):
        #mainpage = urllib.request.urlopen('https://www.straitstimes.com/business/economy?page='+str(pagenum))
        mainPage = urllib.request.urlopen(url+str(pagenum))
        soup = bs.BeautifulSoup(mainPage,'lxml')
        for link in soup.find_all("span", class_="story-headline"):
            #print (link.findChild()['href'])
            stURLsList.append(link.findChild()['href'])

    for link in stURLsList:
        #print (link)
        articlePage = urllib.request.urlopen('https://www.straitstimes.com'+link)
        soup = bs.BeautifulSoup(articlePage,'lxml')

        article = stArticle("title", "author", "date", "content", 'https://www.straitstimes.com'+link)

        #print(soup.find_all('p'))
        contentParent = soup.find_all(attrs={"itemprop":"articleBody"})
        for eleParent in contentParent:
            for eleChild in eleParent.find_all('p'):
                #print(ele.text)
                ###### HELP #### somehow got "content" inserted
                if eleChild.text != "content":
                    article.content = article.content + "\n" + eleChild.text
        
        #print (article.content)
        article.title = soup.find_all(attrs={"itemprop":"name"})[0]['content']
        if not soup.find("meta", property="article:author") is None:
            article.author = soup.find("meta", property="article:author")['content']
        else:
            article.author = "Not available"
        article.date = soup.find(attrs={"property":"article:published_time"})['content']
        stArticlesList.append(article)

    return stArticlesList

################################################################
def todayCrawl(keyword,pageCount):
    #todayURLsList = []
    todayArticlesList = []
    for pagenum in range(pageCount):
        url = "https://www.todayonline.com/json-solr/"+ keyword + "/search?&page=" + str(pagenum)
        html = urllib.request.urlopen(url).read()
        soup = bs.BeautifulSoup(html,'html.parser')
        url_json = json.loads(soup.text)

        #print(url_json)
        for node in url_json['nodes']:
            article = todayArticle("title", "author", "date", "content", "link")
            if not node.get('node').get('author') is "":
                article.author = node.get('node').get('author')
            else:
                article.author = "Not available"
            article.date = node.get('node').get('publication_date')
            article.title = node.get('node').get('title')
            article.url = node.get('node').get('node_url')
            #print(node.get('node').get('title'))

            articleURL = "https://www.todayonline.com/api/v3/article/" + node.get('node').get('node_id')
            #print(articleURL)
            articleHTML = urllib.request.urlopen(articleURL).read()
            articleSoup = bs.BeautifulSoup(articleHTML,'html.parser')
            ArticleURL_Json = json.loads(articleSoup.text)
            articleContent = ArticleURL_Json.get('node').get('body')

            #cleaning of content
            clean = re.compile('<.*?>')
            articleContent = re.sub(clean, '', articleContent)
            articleContent = re.sub('&nbsp;', ' ', articleContent)
            articleContent = re.sub('\n', ' ', articleContent)
            articleContent =  re.sub(' +', ' ', articleContent)
            article.content = articleContent
            #print(articleContent)
            todayArticlesList.append(article)

    # for a in todayArticlesList:
    #     articlePage = urllib.request.urlopen(a.url)
    #     soup = bs.BeautifulSoup(articlePage,'lxml')
    #     contentParent = soup.find_all('p', class_='article-detail_body')

    #     for eleParent in contentParent:
    #         #print(ele.text)
    #         ###### HELP #### somehow got "content" inserted
    #         if eleParent.text != "content":
    #             article.content = article.content + "\n" + eleParent.text        
    #     print(soup)




    return todayArticlesList


test = stCrawl("https://www.straitstimes.com/business/economy?page=",1)
for a in test:
    print(a.title)
    print(a.author)
    #print(a.content[7:-1])
    print(a.date)



test = todayCrawl("health",1)
for a in test:
    print(a.title)
    print(a.author)
    #print(a.content[7:-1])
    print(a.date)
    print(a.url)
    print("\n")
