from flask import Blueprint, request
from app import db

from app.mod_stocks.service import StatisticsService

mod_stocks = Blueprint('stocks', __name__, url_prefix='/stocks')

@mod_stocks.route('/', methods=['GET', 'POST'])
def get_index():
    return "BMV Stocks"


@mod_stocks.route('/statistics/<stock>', methods=['GET', 'POST'])
def market_rates(stock):
    return StatisticsService(stock).get_statistcs()

