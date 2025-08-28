from flask import Flask, render_template
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

def main():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '5000',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
if __name__ == "__main__":
    main()