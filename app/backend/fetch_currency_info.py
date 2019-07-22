import requests
import json

def get_current_rate(base_currency, currency):
    # Get exchange rates
    url = f'https://api.exchangeratesapi.io/latest?base={base_currency}'
    response = requests.get(url)
    code = response.status_code
    response_json = response.json()
    rate = response_json['rates'][currency]
    print(rate)
    return rate

"""
def get_news():
    api_key = "7d7c187e003c460da6d354982f5a7c8b"
    url = (f'https://newsapi.org/v2/everything?sources=financial-post&q=dollar&from=2019-02-17&sortBy=popularity&apiKey={api_key}')
    response = requests.get(url)
    response_json = response.json()
    articles = response_json['articles']
    for a in articles:
        print(a['title'])
"""
