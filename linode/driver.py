import news as news
import time
import datetime
from datetime import date, timedelta



def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

companies = ['Facebook', 'Twitter', 'Netflix', 'Electronic Arts', 'Activision Blizzard',
            '', ' Accenture Plc', 'Microsoft Corporation', 'Oracle Corporation', 'Adobe Inc']
startDate = date(2015,12,1)
endDate = date.today();

with open('data.csv', 'w') as data:
    for company in companies:
        print(company)
        for d in daterange(startDate, endDate):
            print(d)
            s = news.getSentimentByDay(company, d)
            data.write(company + ',' + str(d)  + ',' + str(s[0]) +','+ str(s[1]) + ',' + str(s[2]) + '\n' )
            	
