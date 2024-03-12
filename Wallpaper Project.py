import requests
import bs4

def print_article_info():
    print(end="\n")
    print("Article: %s" %i)
    print(pointer_to_articles)
    print(end="\n")

result = requests.get("http://Speedhunters.com")
soup = bs4.BeautifulSoup(result.text, "lxml")
article_finder = soup.select('.content-thumbnail')

i = 0

for articles in article_finder:
    pointer_to_articles = articles['href'] #this will print all the individual article links
    article_parser = requests.get(pointer_to_articles) # this will parse all of the links from above
    article_soup = bs4.BeautifulSoup(article_parser.text, 'lxml') # This will use bs4 to translate everything into html
    picture_finder = article_soup.select('.alignnone')
    i += 1
    print_article_info()
    for pic_url in picture_finder:
        print (pic_url['data-go-fullscreen'])