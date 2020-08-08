
import newspaper
# import nltk
# nltk.download('punkt')

URL = "http://reuters.com/reuters/topNews"


def scrap_news(url=URL):
    paper = newspaper.build(url, memoize_articles=False)
    article_list = []
    for article in paper.articles:
        article.download()
        article.parse()
        if article.publish_date:
            article.nlp()
            article_list.append((article.url, article.title, article.summary, article.publish_date))
    return article_list
