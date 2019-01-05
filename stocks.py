import urllib.request
import json
import time
import datetime
import platform
import os

symbols = ['BND', 'VOO', 'VTI']


def get_json(url):
    request_urlopen = urllib.request.urlopen(url)
    response = request_urlopen.read().decode("utf-8")
    return json.loads(response)


def write_quote(sym, company, dt, tm, price, chg, chg_p):
    php_out.write('<div class="w3-card-4 w3-margin w3-white">' +
                  company + ' (' +
                  sym + ') ' + ' - <a href="https://iextrading.com/developer/" target="_blank">IEX Trading</a>\n')
    php_out.write('<div class ="w3-container">\n')
    php_out.write('<h5><b>' + price + ' ' + chg + ' (' + chg_p + ')' + '</h5></b>\n')
    php_out.write(dt + " " + tm + '\n')
    php_out.write('</div>\n')
    php_out.write('</div>\n')


if platform.system() == "Linux":
    path = "/opt/bitnami/apache2/htdocs/mattbauman.com/briefing/"
else:
    path = "C:/Users/matt/Desktop"

completeName = os.path.join(path, "stocks.php")
php_out = open(completeName, "w")

# Delayed Quote
quote_success = False
delayed_quote_success = False
for symbol in symbols:
    # Quote
    try:
        quote = get_json("https://api.iextrading.com/1.0/stock/" + symbol + "/quote?displayPercent=true")
        quote_success = True
    except:
        print(symbol + ": fail quote")

    # Delayed Quote
    try:
        delayed_quote = get_json("https://api.iextrading.com/1.0/stock/" + symbol + "/delayed-quote")
        delayed_quote_success = True
    except:
        print(symbol + ": fail delayed_quote")
    if quote_success and symbol == quote['symbol']:
        companyName = quote['companyName']
        change = quote['change']
        changeStr = str(change)
        changePercent = quote['changePercent']
        changePercentStr = str(round(changePercent, 2)) + "%"
    if delayed_quote_success and symbol == delayed_quote['symbol']:
        delayedPrice = delayed_quote['delayedPrice']
        delayedPriceTimeStr = str(delayed_quote['delayedPriceTime'])
        delayedPriceTimeInt = int(delayedPriceTimeStr[0:10])
        delayedPriceDateTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(delayedPriceTimeInt))
        delayedPriceDate = delayedPriceDateTime[0:10]
        delayedPriceTime = delayedPriceDateTime[11:16]
        delayedPriceTime = datetime.datetime.strptime(delayedPriceTime, '%H:%M').strftime('%I:%M %p')
        delayedPriceStr = '${:,.2f}'.format(delayedPrice)
    try:
        write_quote(symbol, companyName, delayedPriceDate, delayedPriceTime, delayedPriceStr, changeStr,
                    changePercentStr)
    except:
        print("fail print")
