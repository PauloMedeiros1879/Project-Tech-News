from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    """Seu código deve vir aqui"""
    search_data = search_news(
        {"title": {"$regex": f"{title}", "$options": "i"}}
    )
    response = []
    for data in search_data:
        response.append(
            (data["title"], data["url"]),
        )
    return response


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
