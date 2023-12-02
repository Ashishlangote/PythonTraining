import requests


# r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2023-09-27&to=2023-09-28&sortBy=popularity&language=en&apiKey=dca9af7ab4144e8ba53639f434ea8f0a')
#
# content = r.json()
# articles = content.get('articles')
# for article in articles:
#     print(f"Title: {article.get('title')}\nDescription: {article.get('description')}")

def get_news(topic, from_date, to_date, language='en', api_key='dca9af7ab4144e8ba53639f434ea8f0a'):
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}8&sortBy=popularity&language={language}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"Title: {article.get('title')}, Description: {article.get('description')}")
    return results


# NOTE: Change the from_date and to_date below to reflect recent dates
# Otherwise, you will get an error.
print(get_news(topic='space', from_date='2023-09-27', to_date='2023-09-29'))
