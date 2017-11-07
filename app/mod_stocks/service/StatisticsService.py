import json
from util.stock import BMV


stock_dict = {
    "AC": "AC-6081"
}


class StatisticsService(object):

    found = None
    bmv = None
    stock_id = None

    def __init__(self, stock):
        self.found = stock in stock_dict
        self.bmv = BMV() if self.found else None
        self.stock_id = stock_dict.get(stock) if self.found else None

    def get_statistcs(self):
        if not self.found:
            return json.dumps(
                {"error": "stock not found"}
            )
        return self.bmv.get_bmv_statistics(self.stock_id).jsonify()
