from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='f4cb02cee2ba4876b22e5fd36342e430')
all_articles = newsapi.get_everything(q='Apple Inc.',
    category='business',
    language='en',
    sort_by='relevancy',
    page=2)
data = [x['description'] for x in all_articles['articles']]
# /v2/top-headlines
print(data)
# /v2/everything

