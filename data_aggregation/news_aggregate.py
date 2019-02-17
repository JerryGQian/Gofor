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
'''
def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
        	return resp.content
    except RequestException as e:
        print('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def build_vector(parsed_json):
	vector = [0] * 4

	currentDT = datetime.datetime.now()
	newsDT_string = parsed_json[0]['datetime']
	newsDT = datetime.datetime(int(newsDT_string[0:4]), int(newsDT_string[5:7]), int(newsDT_string[8:10]), int(newsDT_string[11:13]), int(newsDT_string[14:16]), 0, 1)
	diffDT = currentDT - newsDT
	days = diffDT.days
	hours, remainder = divmod(diffDT.seconds, 3600)
	minutes, seconds = divmod(remainder, 60)
	
	vector[0] = ""
	if days != 0:
		vector[0] += str(days) + "d "
	if hours != 0:
		vector[0] += str(hours) + "h "
	if minutes != 0:
		vector[0] += str(minutes) + "m "
	if seconds != 0:
		vector[0] += str(seconds) + "s "

	vector[0] += "ago"

	vector[1] = parsed_json[0]['headline']
	vector[2] = parsed_json[0]['url']
	vector[3] = parsed_json[0]['source']

	return vector

def create(symbol):
	url = "https://api.iextrading.com/1.0/stock/" + symbol + "/news"
	json_string = simple_get(url)
	parsed_json = json.loads(json_string)

	vec = build_vector(parsed_json)
	dictionary = {"time": vec[0], "headline": vec[1], "url": vec[2], "source": vec[3]}
	json_list = [dictionary]

	#print(json.dumps(json_list))

	return json.dumps(json_list)

#create("aapl")