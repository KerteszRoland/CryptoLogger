EQUAL_CHARACTER = ":=="
SPLIT_CHARACTER = ";"
EMAIL_CRED_FILE = "email_credentials.txt"
EMAIL_FILE = "email.txt"
CRYPTO_FILE = "crypto.txt"
CRYPTO_API_FILE = "coingecko_api.txt"


def ConvertStringArrayToFloatList(arr):
    temp = list()
    for element in arr:
        temp.append(float(element))
    return temp


def GetArrayValues(file, trigger_word):
    with open(file, "r") as file:
        for row in file.read().splitlines():
            if trigger_word + EQUAL_CHARACTER in row:
                values_str = row.split(EQUAL_CHARACTER)[1]
                values_str_arr = values_str.split(SPLIT_CHARACTER)
                return values_str_arr


def GetCryptoAPIHost():
    return GetValue(CRYPTO_API_FILE, "x_rapidapi_host")


def GetCryptoAPIKey():
    return GetValue(CRYPTO_API_FILE, "x_rapidapi_key")


def GetCryptoAPIURL():
    return GetValue(CRYPTO_API_FILE, "url")


def GetValue(file, trigger_word):
    with open(file, "r") as file:
        for row in file.read().splitlines():
            if trigger_word + EQUAL_CHARACTER in row:
                value = row.split(EQUAL_CHARACTER)[1]
                return value


def GetCurrency():
    return GetValue(CRYPTO_FILE, "currency")


def GetCoinsValue():
    str_arr = GetArrayValues(CRYPTO_FILE, "coins_value")
    float_arr = ConvertStringArrayToFloatList(str_arr)
    return float_arr


def GetCoinsAmount():
    str_arr = GetArrayValues(CRYPTO_FILE, "coins_amount")
    float_arr = ConvertStringArrayToFloatList(str_arr)
    return float_arr


def GetSwingPercentThresholds():
    str_arr = GetArrayValues(CRYPTO_FILE, "swing_percent_threshold")
    float_arr = ConvertStringArrayToFloatList(str_arr)
    return float_arr


def GetCoins():
    return GetArrayValues(CRYPTO_FILE, "coins")


def GetToEmailAddress():
    return GetValue(EMAIL_CRED_FILE, "to_email_address")


def GetFromEmailAddress():
    return GetValue(EMAIL_CRED_FILE, "from_email_address")


def GetEmailPassword():
    return GetValue(EMAIL_CRED_FILE, "password")


def GetSMTPEmail():
    return GetValue(EMAIL_CRED_FILE, "smtp_email")


def GetTimeInterval():
    return int(GetValue(EMAIL_CRED_FILE, "time_interval_seconds"))


def GetEmailTitle():
    return GetValue(EMAIL_FILE, "title")


def GetEmailText():
    text = ""
    with open(EMAIL_FILE, "r") as file:
        for row in file.readlines():
            if EQUAL_CHARACTER not in row:
                text += row
    return text


def PrintAllInfo():
    print(GetCoins())
    print(GetSwingPercentThresholds())
    print(GetCoinsAmount())
    print(GetCoinsValue())
    print(GetCurrency())
    print()
    print(GetSMTPEmail())
    print(GetToEmailAddress())
    print(GetFromEmailAddress())
    print(GetEmailPassword())
    print(GetTimeInterval())
    print()
    print(GetCryptoAPIURL())
    print(GetCryptoAPIKey())
    print(GetCryptoAPIHost())
    print()
    print(GetEmailTitle())
    print(GetEmailText())


# PrintAllInfo()
