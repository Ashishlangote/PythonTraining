import requests


def get_news(country, api_key='dca9af7ab4144e8ba53639f434ea8f0a'):
  url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
  r = requests.get(url)
  content = r.json()
  articles = content['articles']
  results = []
  for article in articles:
    results.append(f"Title: {article.get('title')}, Description: {article.get('description')}")
  return results

print(get_news(country='us'))



