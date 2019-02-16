from requests import get
from requests.exceptions import RequestException
from contextlib import closing
import json

#INSTALL REQUESTS >> pip install requests BeautifulSoup4

def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
        	return resp.content
    except RequestException as e:
        print('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

url = "https://api.iextrading.com/1.0/stock/aapl/chart/5y"
json_string = simple_get(url)
parsed_json = json.loads(json_string)

def build_input_vector(day_to_predict):
	vector = [0] * 306
	for i in range(1, 301, 3):
		day = day_to_predict - (int)((i + 3) / 3)
		vector[i] = parsed_json[day]['low']
		vector[i+1] = parsed_json[day]['high']
		vector[i+2] = parsed_json[day]['close']

	#Mark data here
	
	vector[304] = (int)(parsed_json[day_to_predict]['date'][8:10])
	vector[305] = (int)(parsed_json[day_to_predict]['date'][5:7])

	return vector

def build_output_vector(day_to_predict):
	day = len(parsed_json)-1-day_to_predict
	return [parsed_json[day]['low'], parsed_json[day]['high'], parsed_json[day]['close']]


def create():
	input_vec_list = []
	output_vec_list = []

	for day_to_predict in range(0, 1000):
		input_vec = build_input_vector(day_to_predict)
		output_vec = build_output_vector(day_to_predict)
		print(input_vec)
		print(output_vec)
		input_vec_list.append(input_vec)
		output_vec_list.append(output_vec)

	input_output_list_tuple = (input_vec_list, output_vec_list)

	return input_output_list_tuple

create()