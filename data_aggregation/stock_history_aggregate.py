from requests import get
from requests.exceptions import RequestException
from contextlib import closing
import json

'''INSTALL REQUESTS >> pip install requests BeautifulSoup4'''

def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
        	return resp.content

    except RequestException as e:
        print('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def build_vector(url) {
	json_string = simple_get(url)
	parsed_json = json.loads(json_string)

	
	for 
}

url = "https://api.iextrading.com/1.0/stock/aapl/chart/1y"
print(build_vector(url))


print(parsed_json[1], "\n")
print(parsed_json[3]['date'])
print(parsed_json[2]['date'])
print(parsed_json[1]['date'])
print(parsed_json[1]['open'])
print(parsed_json[1]['low'], "-", parsed_json[1]['high'])
print(parsed_json[1]['close'])