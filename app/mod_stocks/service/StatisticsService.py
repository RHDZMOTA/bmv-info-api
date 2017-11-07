from util.stock import BMV


stock_dict = {
    "AC": "AC-6081"
}

class StatisticsService(object):

    def __init__(self, stock):
        self.bmv = BMV()
        self.stock_id = stock_dict.get(stock)

    def get_url(self, stock_id):
        return "https://www.bmv.com.mx/en/issuers/statistics/{}".format(stock_id)

    def get_statistcs(self):
        return self.bmv.get_bmv_statistics(self.get_url(self.stock_id)).jsonify()