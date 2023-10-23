from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
nomi=[]
linki=[]
import requests 
from bs4 import BeautifulSoup 
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    k=0
    qidirish = update.message.text.split()[1]
    URL = f"https://kun.uz/news/search?q={qidirish}"
    r = requests.get(URL) 
    soup = BeautifulSoup(r.content, 'html.parser')
    news = soup.find_all("div", class_="col-md-4")
    for item in news:
        news_name = item.find('a', class_='news__title').text
        news_link = item.find('a', class_='news__title')['href']
        nomi.append(news_name)
        linki.append(news_link)
    while k<len(nomi):
        await update.message.reply_html(
        rf"{nomi[k]} -  {linki[k]}",
    )
        k+=1
def main() -> None:
    """Start the bot."""
    application = Application.builder().token("6955557298:AAF6hZnyRuvbwN_tyjmYRAH2UYbIzwulAhg").build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling(allowed_updates=Update.ALL_TYPES)
if __name__ == "__main__":
    main()

