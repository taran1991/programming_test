
from pymongo import MongoClient
import scraping


def save_news_to_mongodb(news):
    client = MongoClient('localhost', 27017)
    news_db = client['news']
    news_col = news_db['news']
    for novelty in news:
        post = dict(zip(['url', 'title', 'short_description', 'publish_date'], novelty))
        news_col.insert_one(post)


if __name__ == '__main__':
    news = scraping.scrap_news()
    save_news_to_mongodb(news)
