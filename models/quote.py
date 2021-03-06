import json
from apiTools import *

class Quote:
    def __init__(self, close, coupon, date, gross, high, low, nav, ope, pl, ret, volume):
        self.close = close
        self.coupon = coupon  
        self.gross = gross
        self.high = high
        self.low = low 
        self.nav = nav
        self.ope = ope
        self.pl = pl
        self.ret = ret
        self.volume = volume
    
    def print_info(self):
        print("close " + str(self.close))
        print("coupon " + str(self.coupon))
        print("gross " + str(self.gross))
        print("high " + str(self.high))
        print("low " + str(self.low))
        print("nav " + str(self.nav))
        print("open " + str(self.ope))
        print("pl " + str(self.pl))
        print("return " + str(self.ret))
        print("close " + str(self.volume))

    
def asset_to_quotes(asset, in_portfolio, start_date: str = "1985-04-12", end_date: str = "2020-11-17"):
    obj_quotes = []

    if in_portfolio:
        result = get_quotes(asset, start_date, end_date)
    else:
        result = get_quotes(asset['ASSET_DATABASE_ID']['value'], start_date, end_date)
        
    quotes = json.loads(result)

    for quote in quotes:
        close = quote.get('close', 'none')
        coupon = quote.get('coupon', 'none')
        date = quote.get('date', 'none')
        gross = quote.get('gross', 'none')
        high = quote.get('high', 'none')
        low = quote.get('low', 'none')
        nav = quote.get('nav', 'none')
        op = quote.get('open', 'none')
        pl = quote.get('pl', 'none')
        ret = quote.get('ret', 'none')
        volume = quote.get('volume', 'none')
            
        new_quote = Quote(close, coupon, date, gross, high, low, nav, op, pl, ret, volume)
        obj_quotes.append(new_quote)

    return obj_quotes

