from tech_news.database import search_news
from datetime import datetime


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
    try:
        data = datetime.strptime(date, "%Y-%m-%d").date()
        news_date = data.strftime("%d/%m/%Y")
        search_data = search_news({"timestamp": {"$regex": news_date}})
        response = []
        for data in search_data:
            response.append((data["title"], data["url"]))
        return response
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    news_category = search_news(
        {"category": {"$regex": f"{category}", "$options": "i"}}
    )
    response = []
    for data in news_category:
        response.append(
            (data["title"], data["url"]),
        )
    return response
