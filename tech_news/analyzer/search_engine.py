from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(new["title"], new["url"]) for new in news]


# Requisito 7
def search_by_date(date):
    try:
        date_input = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        Query = {"timestamp": {"$regex": date_input}}
        news = search_news(Query)
        results = [(new["title"], new["url"]) for new in news]
        return results
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    news = search_news({"tags": {"$regex": tag, "$options": "i"}})
    results = [(new["title"], new["url"]) for new in news]
    return results


# Requisito 9
def search_by_category(category):
    news = search_news({"category": {"$regex": category, "$options": "i"}})
    results = [(new["title"], new["url"]) for new in news]
    return results
