from requests import get
from requests.exceptions import RequestException
from contextlib import closing
import json
import predictor
import datetime

#INSTALL REQUESTS >> pip install requests

#CONFIGURABLE ############################################
symbols = ["googl", "goog", "qcom", "aapl", "amzn", "msft", "fb", "twtr", "nflx", "tsla", "cof", "orcl", "adbe", "amd", "nvda", "intc" ]
##########################################################

def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
        	return resp.content
    except RequestException as e:
        print('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def build_input_vector(day_to_predict, parsed_json, company_id):
	vector = [0] * 303
	vector[0] = company_id
	for i in range(1, 301, 3):
		day = len(parsed_json)-1-day_to_predict - (int)((i + 3) / 3)
		vector[301 - i] = parsed_json[day]['low']
		vector[301 - (i+1)] = parsed_json[day]['high']
		vector[301 - (i+2)] = parsed_json[day]['close']
	
	vector[301] = (int)(parsed_json[day_to_predict]['date'][8:10])
	vector[302] = (int)(parsed_json[day_to_predict]['date'][5:7])

	return vector


def create():
	prediction_vec_list = []

	url1 = "https://api.iextrading.com/1.0/stock/" + symbols[0] + "/chart/5y"
	json_string1 = simple_get(url1)
	parsed_json1 = json.loads(json_string1)

	date_string = parsed_json1[len(parsed_json1)-1]['date']
	lastday = datetime.datetime(int(date_string[0:4]), int(date_string[5:7]), int(date_string[8:10]))
	prediction_day = datetime.datetime(int(date_string[0:4]), int(date_string[5:7]), int(date_string[8:10])) 
	
	if lastday.weekday() >= 4 and lastday.weekday() <= 6:
		prediction_day += datetime.timedelta(days=(7 - lastday.weekday()))  
	
	prediction_day_string = str(prediction_day.month) + "-" + str(prediction_day.day) + "-" + str(prediction_day.year)

	for i in range(0, len(symbols)):
		url = "https://api.iextrading.com/1.0/stock/" + symbols[i] + "/chart/5y"
		json_string = simple_get(url)
		parsed_json = json.loads(json_string)

		input_vec = build_input_vector(0, parsed_json, i)
		prediction_vec = predictor.predict_stock(input_vec)

		predictionary = {"symbol": symbols[i], "date": prediction_day_string, "low": prediction_vec[0], "high": prediction_vec[1], "close": prediction_vec[2], }
		prediction_vec_list.append(predictionary)
	
	#print(json.dumps(prediction_vec_list))

	return json.dumps(prediction_vec_list)

create()