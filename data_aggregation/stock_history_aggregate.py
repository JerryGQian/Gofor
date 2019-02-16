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


url = "https://api.iextrading.com/1.0/stock/aapl/chart/1d"
print(simple_get(url))
json_string = simple_get(url)

print("\n\n")

parsed_json = json.loads(json_string)
print(parsed_json[1])