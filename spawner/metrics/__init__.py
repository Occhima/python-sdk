import requests
import json
import pandas 


class APIMetrics:
    def __init__(self, ticker, date, token):

        #validation required
        if not isinstance((ticker, date, token), ()):
            raise ValueError

        self._ticker = ticker
        self._date = date
        self._token = token
        self._url = url = "https://spawnerapi.com/sharpe/" + ticker + "/" + date + "/" + token
        self.response = requests.get(url).text


    def sharpe(token, ticker, date): 
        return round(float(response),2)

    def volatility(token, ticker, date): 
        return round(float(response), 2)

    def expected_return(token, ticker, date): 
        return round(float(response),2)

    def kelly_criterion(token, ticker): 
        return round(float(response),2)

