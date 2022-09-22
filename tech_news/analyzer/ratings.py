from tech_news import database


# Requisito 10
def top_5_news():
    news = database.find_news()
    results = []
    order = sorted(news, key=lambda n: (-n["comments_count"], n["title"]))

    for n in order:
        results.append((n["title"], n["url"]))

    return results[:5]


# Requisito 11
def top_5_categories():
    news = database.find_news()
    categories = [new["category"] for new in news]
    sort_categories = sorted(
        set(categories),
        key=lambda category: (-categories.count(category), category)
    )
    return sort_categories[:5]
