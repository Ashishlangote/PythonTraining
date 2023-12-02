import requests

r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2023-09-27&to=2023-09-28&sortBy=popularity&language=en&apiKey=dca9af7ab4144e8ba53639f434ea8f0a')
#
content = r.json()
# print(content)
print(content['articles'][0]['description'])