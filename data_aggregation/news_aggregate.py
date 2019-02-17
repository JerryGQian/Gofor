from requests import get
from requests.exceptions import RequestException
from contextlib import closing
import json
import datetime


#INSTALL REQUESTS >> pip install requests
#CONFIGURABLE ############################################
symbols = ["googl", "qcom", "aapl", "amzn", "msft", "fb", "twtr", "nflx", "tsla", "cof", "orcl", "adbe", "amd", "nvda", "intc" ]
##########################################################
'''
2019-02-16 22:37:14.354720
2019-02-16 22:37:14.658937
2019-02-16 22:37:17.845163
2019-02-16 22:37:18.021085
2019-02-16 22:37:18.282451
2019-02-16 22:37:18.456986
2019-02-16 22:37:18.653458
2019-02-16 22:37:18.856914
2019-02-16 22:37:19.095312
'''
def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
        	return resp.content
    except RequestException as e:
        print('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def build_input_vector(parsed_json):
	vector = [0] * 4

	currentDT = datetime.datetime.now()
	newsDT = parsed_json[0]['datetime']
	diff_hour = currentDT.hour - (int)(newsDT[11:13])
	diff_minute = currentDT.minute - (int)(newsDT[14:16])
	if diff_hour == 0:
		vector[0] = str(diff_minute) + "s ago"
	else:
		vector[0] = str(diff_hour) + "h " + str(diff_minute) + "s ago"
	vector[1] = parsed_json[0]['headline']
	vector[2] = parsed_json[0]['source']
	vector[3] = parsed_json[0]['url']

	return vector

def create():
	company_news_vec_list = []

	for i in range(0, len(symbols)):
		url = "https://api.iextrading.com/1.0/stock/" + symbols[i] + "/news"
		json_string = simple_get(url)
		parsed_json = json.loads(json_string)

		
		vec = build_input_vector(parsed_json)
		company_news_vec_list.append(vec)
	print(company_news_vec_list)

	return company_news_vec_list

create()