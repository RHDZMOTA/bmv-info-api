import json
from util.stock import BMV
from data import get_allowed_data


class StatisticsService(object):

    found = False
    bmv = None
    stock_id = None

    def __init__(self, stock):
        self.found = stock in get_allowed_data()
        self.bmv = BMV() if self.found else None
        self.stock_id = stock if self.found else None

    def get_statistcs(self):
        if not self.found:
            return json.dumps(
                {
                    "error": "stock not found",
                    "allowed_stocks": get_allowed_data()
                 }
            )
        stats = self.bmv.get_bmv_statistics(self.stock_id).jsonify()
        self.bmv.close_connection()
        return stats
