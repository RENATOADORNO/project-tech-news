import sys

from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category
    )
from tech_news.analyzer.ratings import top_5_news, top_5_categories


def return_news():
    qtd_news = int(input("Digite quantas notícias serão buscadas:"))
    print(get_tech_news(qtd_news))


def news_by_title():
    news_title = input("Digite o título:")
    print(search_by_title(news_title))


def news_by_date():
    news_date = input("Digite a data no formato aaaa-mm-dd:")
    print(search_by_date(news_date))


def news_by_tag():
    news_tag = input("Digite a tag:")
    print(search_by_tag(news_tag))


def news_by_category():
    news_category = input("Digite a categoria:")
    print(search_by_category(news_category))


def list_top_5_news():
    print(top_5_news())


def list_top_5_categories():
    print(top_5_categories())


options = [
        return_news,
        news_by_title,
        news_by_date,
        news_by_tag,
        news_by_category,
        list_top_5_news,
        list_top_5_categories,
    ]


def validate_option(option):
    if option == '':
        options[0]
    elif int(option) == 7:
        print("Encerrando script\n")
    elif int(option) in range(0, 7):
        options[int(option)]()
    else:
        sys.stderr.write("Opção inválida\n")


# Requisito 12
def analyzer_menu():
    option_menu = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair.")

    validate_option(option_menu)


if __name__ == "__main__":
    analyzer_menu()
