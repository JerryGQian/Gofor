import requests
import json
import numpy as np
import datetime
from datetime import date
import time

def avgNewsSentiment(query, start, end, alexaMin):
    (query, start, end, alexaMin) = (str(query), str(start), str(end), str(alexaMin))
    query = query.replace(' ', '_')
    url = 'https://api.newsapi.aylien.com/api/v1/trends?field=sentiment.title.polarity&text='+query+'&published_at.start=NOW-'+start+'DAYS%2FDAY&published_at.end=NOW-'+end+'DAYS&sort_by=recency&source.rankings.alexa.rank.max='+alexaMin
    headers = {'X-AYLIEN-NewsAPI-Application-ID': '78485f1f', 'X-AYLIEN-NewsAPI-Application-Key' : 'ae91ef5301b7300b033330bd3527bb31'}
    print(url)
    response = requests.get(url, headers=headers).json()
    sentiment = [-1, -1, -1]
    if 'trends' not in response:
        for i in range(100):
            time.sleep(1)
            print('Retry')
            response = requests.get(url, headers=headers).json()
            if 'trends' in response:
                break
            elif i == 99:
                return sentiment
    
    response = response['trends']
    sent_raw = [response[1]['count'], response[0]['count'], response[2]['count']]
    norm = np.linalg.norm(sent_raw)
    sentiment = [x / norm for x in sent_raw]
    return sentiment

def getSentimentByDay(query, day):
    today = date.today()
    d0 = today - day
    if day.day == 1:
        time.sleep(5)
    sentiment = avgNewsSentiment(query, d0.days+5, d0.days, 5000)
    print(sentiment)
    return sentiment

getSentimentByDay('Google', date(2015, 12, 1))


