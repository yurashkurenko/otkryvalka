import requests

# История платежей - сумма за диапазон дат
def payment_history_summ_dates(api_access_token):
    s = requests.Session()
    url='https://web.totalcoin.io/?api-key='
#    s.headers['authorization'] = 'api-key ' + api_access_token
    h = s.get(url)
    return h
#https://web.totalcoin.io/?s=1&utm_source=totalcoin.io&utm_medium=home#/settings

api_access_token=''
#https://web.totalcoin.io/?api-key=#/dashboard

print(payment_history_summ_dates(api_access_token).text)
