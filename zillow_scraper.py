import requests
from flask import Flask, jsonify

app = Flask(__name__)
API_KEY = 'd6d7920e-6535-43a6-b11c-af40604a081c'
LISTING_URL = 'https://www.zillow.com/los-angeles-ca/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A55.89449180093996%2C%22east%22%3A-58.830708375000015%2C%22south%22%3A12.930823520220883%2C%22west%22%3A-133.537739625%7D%2C%22mapZoom%22%3A4%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12447%2C%22regionType%22%3A6%7D%2C%7B%22regionId%22%3A6181%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22days%22%7D%7D%2C%22isListVisible%22%3Atrue%7D'

@app.route('/api/listings', methods=['GET'])
def get_listings():
    url = 'https://app.scrapeak.com/v1/scrapers/zillow/listing'
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    params = {
        'api_key': API_KEY,
        'url': LISTING_URL
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run()
