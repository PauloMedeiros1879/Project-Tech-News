import requests
import time
import parsel

from tech_news.database import create_news


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, headers={"user-agent": "Fake user-agent"})
        time.sleep(1)
        response.raise_for_status()
        return response.text
    except (requests.HTTPError, requests.ReadTimeout):
        return None


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(html_content)
    """Todos os links tem a classe cs-overlay-link,
    então capturei todos os links que tenham essa classe"""
    url = selector.css(".cs-overlay-link::attr(href)").getall()
    return url


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(html_content)

    next_page = selector.css(".next.page-numbers::attr(href)").get()
    if next_page:
        return next_page
    return None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(html_content)

    response = {
        "url": selector.css("link[rel='canonical']::attr(href)").get(),
        "title": selector.css("h1.entry-title::text").get().strip(),
        "timestamp": selector.css("li.meta-date::text").get(),
        "writer": selector.css(".author > a::text").get(),
        "reading_time": int(
            selector.css("li.meta-reading-time::text").get()[0:2]
        ),
        "summary": "".join(
            selector.css(".entry-content > p:first-of-type *::text").getall()
        ).strip(),
        "category": selector.css(".label::text").get(),
    }

    return response


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    url = "https://blog.betrybe.com"
    data = []
    while len(data) < amount and url:
        get_page_content = fetch(url)
        get_url_news = scrape_updates(get_page_content)
        for url in get_url_news:
            news_content = fetch(url)
            data.append(scrape_news(news_content))
            if len(data) == amount:
                break
        url = scrape_next_page_link(get_page_content)
    create_news(data)
    return data


get_tech_news(5)
