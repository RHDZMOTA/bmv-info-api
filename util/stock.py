import json
from selenium import webdriver


class BMV(object):

    def __init__(self):
        self.browser = webdriver.PhantomJS()
        self.browser.set_window_size(1120, 550)

    def get_bmv_statistics(self, stock_id):
        url = "https://www.bmv.com.mx/en/issuers/statistics/" + stock_id
        self.browser.get(url)
        market_rates = self.browser.find_element_by_id("tableMarketRates")
        indicators = self.browser.find_element_by_id("tableIndicators")
        return StockStatistics(
            str(stock_id),
            str(market_rates.text),
            str(indicators.text))

    def close_connection(self):
        self.browser.quit()


class StockStatistics(object):

    def __init__(self, stock_id, market_rates_text, indicators_text):
        self.stock_id = stock_id
        self.stock_market_rates = StockMarketRates(market_rates_text)
        self.stock_indicators = StockIndicators(indicators_text)

    def to_dict(self):
        return {
            "stock_id": self.stock_id,
            "stock_market_rates": self.stock_market_rates.to_dict(),
            "stock_indicators": self.stock_indicators.to_dict()
        }

    def jsonify(self):
        return json.dumps(self.to_dict())


class StockIndicators(object):
    price_earnings_ratio = None
    price_book_value_ratio = None
    earnings_per_share = None
    book_value_per_share = None
    shares_outstanding = None

    def __init__(self, text):
        self.text = text
        self.set_price_earnings_ratio()
        self.set_price_book_value_ratio()
        self.set_earnings_per_share()
        self.set_book_value_per_share()
        self.set_shares_outstanding()

    @staticmethod
    def filter_str(text, word, sep="\n"):
        return list(filter(lambda x: word.lower() in x, text.lower().split(sep)))[0]

    def extract_value(self, key_word, text):
        return self.filter_str(text, key_word).replace(key_word.lower(), "").replace(" ", "")

    def set_price_earnings_ratio(self):
        self.price_earnings_ratio = self.extract_value("Price/Earnings Ratio", self.text)

    def set_price_book_value_ratio(self):
        self.price_book_value_ratio = self.extract_value("Price/Book Value Ratio", self.text)

    def set_earnings_per_share(self):
        self.earnings_per_share = self.extract_value("Earnings Per Share Ratio", self.text)

    def set_book_value_per_share(self):
        self.book_value_per_share = self.extract_value("Book Value per Share", self.text)

    def set_shares_outstanding(self):
        self.shares_outstanding = self.extract_value("Shares Outstanding", self.text)

    def to_dict(self):
        return self.__dict__

    def jsonify(self):
        return json.dumps(self.to_dict())

    def to_string(self):
        return self.text


class StockMarketRates(object):

    date = None
    ask_vol = None
    ask_price = None
    bid_vol = None
    bid_price = None
    last_trade_price = None
    prev_price = None
    change = None
    traded_vol = None
    max_price = None
    min_price = None

    def __init__(self, text):
        self.text = text
        self.set_date(text)
        self.set_ask_vol(text)
        self.set_ask_price(text)
        self.set_bid_vol(text)
        self.set_bid_price(text)
        self.set_last_trade_price(text)
        self.set_prev_price(text)
        self.set_change(text)
        self.set_traded_vol(text)
        self.set_max_price(text)
        self.set_min_price(text)

    @staticmethod
    def filter_str(text, word, sep="\n"):
        return list(filter(lambda x: word.lower() in x, text.lower().split(sep)))[0]

    def extract_value(self, key_word, text):
        return self.filter_str(text, key_word).replace(key_word.lower(), "").replace(" ", "")

    def set_date(self, text):
        self.date = self.extract_value("Date", text)

    def set_ask_vol(self, text):
        self.ask_vol = self.extract_value("Ask Volume", text)

    def set_ask_price(self, text):
        self.ask_price = self.extract_value("Ask price", text)

    def set_bid_vol(self, text):
        self.bid_vol = self.extract_value("Bid Volume", text)

    def set_bid_price(self, text):
        self.bid_price = self.extract_value("Bid Price", text)

    def set_last_trade_price(self, text):
        self.last_trade_price = self.extract_value("Last Traded Price", text)

    def set_prev_price(self, text):
        self.prev_price = self.extract_value("Previous Price", text)

    def set_change(self, text):
        self.change = self.extract_value("Change", text)

    def set_traded_vol(self, text):
        self.traded_vol = self.extract_value("Traded Volume", text)

    def set_max_price(self, text):
        self.max_price = self.extract_value("Maximum", text)

    def set_min_price(self, text):
        self.min_price = self.extract_value("Minimum", text)

    def to_dict(self):
        return self.__dict__

    def jsonify(self):
        return json.dumps(self.to_dict())

    def to_string(self):
        return self.text

