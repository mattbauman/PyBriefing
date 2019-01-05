import urllib.request
import json
import time
import datetime


def get_json(url):
    request_urlopen = urllib.request.urlopen(url)
    response = request_urlopen.read().decode("utf-8")
    return json.loads(response)


def write_delayed_quote(sym, dt, tm, price):
    print(sym)
    print(dt)
    print(tm)
    print(price)
    print()


# https://api.iextrading.com/1.0/stock/VOO/chart
# https://api.iextrading.com/1.0/stock/VOO/delayed-quote
# https://api.iextrading.com/1.0/stock/VOO/quote
# https://api.iextrading.com/1.0/stock/aapl/ohlc  #open/close

# Delayed Quote
for symbol in ['BND', 'VOO', 'VTI']:
    try:
        delayed_quote = get_json("https://api.iextrading.com/1.0/stock/" + symbol + "/delayed-quote")
        delayed_quote_success = True
    except:
        delayed_quote_success = False
        print(symbol + ": fail delayed_quote")
    if delayed_quote_success and symbol == delayed_quote['symbol']:
        print(delayed_quote)
        delayedPrice = delayed_quote['delayedPrice']
        delayedPriceTimeStr = str(delayed_quote['delayedPriceTime'])
        delayedPriceTimeInt = int(delayedPriceTimeStr[0:10])
        delayedPriceDateTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(delayedPriceTimeInt))
        delayedPriceDate = delayedPriceDateTime[0:10]
        delayedPriceTime = delayedPriceDateTime[11:16]
        delayedPriceTime = datetime.datetime.strptime(delayedPriceTime, '%H:%M').strftime('%I:%M %p')
        delayedPriceStr = '${:,.2f}'.format(delayedPrice)
        write_delayed_quote(symbol, delayedPriceDate, delayedPriceTime, delayedPriceStr)
    try:
        quote = get_json("https://api.iextrading.com/1.0/stock/" + symbol + "/quote?displayPercent=true")
        quote_success = True
    except:
        quote_success = False
        print(symbol + ": fail previous")
    if delayed_quote_success and symbol == delayed_quote['symbol']:
        change = quote['change']
        changePercent = quote['changePercent']
        print(change)
        print(str(round(changePercent, 2)) + "%")
