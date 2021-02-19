import requests
import mailHandler
import txtHandler
from time import sleep

coins = txtHandler.GetCoins()
swing_percent_threshold = txtHandler.GetSwingPercentThresholds()
coins_amount = txtHandler.GetCoinsAmount()
coins_value = txtHandler.GetCoinsValue()
CURRENCY = txtHandler.GetCurrency()
TIME_INTERVAL = txtHandler.GetTimeInterval()
TO_EMAIL_ADDRESS = txtHandler.GetToEmailAddress()
EMAIL_TITLE = txtHandler.GetEmailTitle()
EMAIL_TEXT = txtHandler.GetEmailText()


def GetCoinPrice(coin, currency):
    url = txtHandler.GetCryptoAPIURL()
    querystring = {"ids": coin, "vs_currencies": currency}
    headers = {
        'x-rapidapi-key': txtHandler.GetCryptoAPIKey(),
        'x-rapidapi-host': txtHandler.GetCryptoAPIHost()
    }
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        json_response = response.json()
        coin_price = json_response[coin][currency]
        return coin_price
    except KeyError:
        print(f"ERROR: {json_response}")


def GetCoinValueInCurrency(coin, amount, currency):
    coin_price = GetCoinPrice(coin, currency)
    return coin_price*amount


def GetCoinSwingPercentage(coin, amount, worth, currency):
    coin_value = GetCoinValueInCurrency(coin, amount, currency)
    swing_percent = ((coin_value-worth)/worth)*100
    if swing_percent > 0:
        swing_percent = f"+{swing_percent}"
    return swing_percent


def IsValueExceededThreshold(value, threshold):
    if 0 < threshold <= value or value <= threshold < 0:
        return True
    else:
        return False


def GetMailText(coin, amount, percent, value, currency, swing_threshold):
    currency = currency.upper()
    text = EMAIL_TEXT.\
        replace("{coin}", str(coin)).\
        replace("{amount}", str(format(amount, '.8f'))).\
        replace("{percent}", str(percent)). \
        replace("{value}", str(format(value, '.8f'))). \
        replace("{currency}", str(currency)). \
        replace("{swing_threshold}", str(swing_threshold))
    return text


def GetMailTitle():
    return EMAIL_TITLE


def TESTSendEmail(email, title, text):
    print()
    print(title)
    print(text)
    print()


def CheckForCoinsSwingPercentage(coins, swing_threshold, coins_amount, coins_value, currency):
    for i in range(0, len(coins)):
        swing_percent_str = GetCoinSwingPercentage(coins[i], coins_amount[i], coins_value[i], currency)
        swing_percent = float(swing_percent_str)
        coin_value = GetCoinValueInCurrency(coins[i], coins_amount[i], currency)

        if IsValueExceededThreshold(swing_percent, swing_threshold[i]):
            title = GetMailTitle()
            text = GetMailText(coins[i], coins_amount[i], swing_percent_str, coin_value, currency, swing_threshold[i])
            mailHandler.SendEmail(TO_EMAIL_ADDRESS, title, text)


def CheckPricesEveryInterval(seconds):
    CheckForCoinsSwingPercentage(coins, swing_percent_threshold, coins_amount, coins_value, CURRENCY)
    sleep(seconds)


while True:
    CheckPricesEveryInterval(TIME_INTERVAL)
