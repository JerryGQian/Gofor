from requests import get
from requests.exceptions import RequestException
from contextlib import closing
import json
import predictor

#INSTALL REQUESTS >> pip install requests

#CONFIGURABLE ############################################
idx = 0
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
	url = "https://api.iextrading.com/1.0/stock/" + symbols[idx] + "/chart/5y"
	json_string = simple_get(url)
	parsed_json = json.loads(json_string)

	input_vec = build_input_vector(3, parsed_json, idx)

	prediction_vec = predictor.predict_stock(input_vec)
	print(prediction_vec)

	return prediction_vec

create()