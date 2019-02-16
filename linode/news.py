import requests
import json
import numpy as np
import datetime

def avgNewsSentiment(query, start, end, alexaMin):
    (query, start, end, alexaMin) = (str(query), str(start), str(end), str(alexaMin))
    query = query.replace(' ', '_')
    url = 'https://api.newsapi.aylien.com/api/v1/trends?field=sentiment.title.polarity&published_at.start=NOW-'+start+'DAYS%2FDAY&published_at.end=NOW-'+end+'DAYS&entities.body.links.dbpedia%5B%5D=http%3A%2F%2Fdbpedia.org%2Fresource%2F'+query+'&sort_by=relevance&source.rankings.alexa.rank.max='+alexaMin
    headers = {'X-AYLIEN-NewsAPI-Application-ID': '78485f1f', 'X-AYLIEN-NewsAPI-Application-Key' : 'ae91ef5301b7300b033330bd3527bb31'}
    response = requests.get(url, headers=headers).json()['trends']
    sent_raw = [response[1]['count'], response[0]['count'], response[2]['count']]
    norm = np.linalg.norm(sent_raw)
    sentiment = [x / norm for x in sent_raw]

    return sentiment
avgNewsSentiment('Apple Inc.', 5, 0, 5000)
