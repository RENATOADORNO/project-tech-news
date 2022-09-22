import requests as req
import time
from parsel import Selector


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
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
