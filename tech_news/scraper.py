import requests as req
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    headers = {'user-agent', 'Fake user-agent'}
    timeout = 3

    try:
        response = req.get(url, headers, timeout)

    except req.ReadTimeout:
        return None

    if response.status_code == 200:
        return response.text

    return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    links = selector.css("div.cs-overlay a::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page = selector.css("a.next.page-numbers::attr(href)").get()
    return next_page


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    result = {}

    result["url"] = selector.css("head link[rel*=canonical]::attr(href)").get()

    header = selector.css("div.entry-header-inner")
    result["title"] = header.css("h1.entry-title::text").get().rstrip()
    result["timestamp"] = header.css("li.meta-date::text").get()
    result["writer"] = header.css("ul.post-meta a.fn::text").get()

    comments = selector.css("ol.comment-list").getall()
    result["comments_count"] = len(comments)

    sumary_path = ".entry-content > p:first-of-type *::text"
    summary = selector.css(sumary_path).getall()
    result["summary"] = "".join(summary).strip()

    result["tags"] = []
    for tag in selector.css("a[rel*=tag]::text").getall():
        result["tags"].append(tag)

    result["category"] = header.css("div.meta-category span.label::text").get()

    return result


# Requisito 5
def get_tech_news(amount):
    list_urls_news = []
    list_content_news = []

    main_news_page = fetch("https://blog.betrybe.com")
    while len(list_urls_news) < amount:
        urls = scrape_novidades(main_news_page)

        for url in urls:
            list_urls_news.append(url)

        next_page = scrape_next_page_link(main_news_page)
        main_news_page = fetch(next_page)

    for url in list_urls_news[:amount]:
        news = fetch(url)
        news_content = scrape_noticia(news)
        list_content_news.append(news_content)

    create_news(list_content_news)

    return list_content_news
