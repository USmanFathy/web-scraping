from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page,'html.parser')
article = soup.find_all(name='a' , class_="story link")
article_texts =[]
article_links=[]

for article_tag in article :
    text= article_tag.getText()
    article_texts.append(text)
    link= article_tag.get('herf')
    article_links.append(link)


article_votes = [int(score.getText().split()[0])for score in soup.find_all(name="span",class_='score')]


