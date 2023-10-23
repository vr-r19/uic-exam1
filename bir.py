import requests 
from bs4 import BeautifulSoup 
URL = "https://kun.uz"
r = requests.get(URL) 
soup = BeautifulSoup(r.content, 'html.parser')
news = soup.find_all("a", class_="news-lenta")
for i in news:
    print(f"{i.text} - {i['href']}")
    print()
