import requests

# История платежей - сумма за диапазон дат
def payment_history_summ_dates(api_access_token):
    s = requests.Session()
    url='https://web.totalcoin.io/?api-key=6f936af551561fdf8eec708719e1e0fe12b9556b660a6d05a767dd12b242f5cbf4aa6b91a7a9cc26db0644819c092e3eae0c69385caa5a7b07da0d956da81981'
#    s.headers['authorization'] = 'api-key ' + api_access_token
    h = s.get(url)
    return h
#https://web.totalcoin.io/?s=1&utm_source=totalcoin.io&utm_medium=home#/settings

api_access_token='6f936af551561fdf8eec708719e1e0fe12b9556b660a6d05a767dd12b242f5cbf4aa6b91a7a9cc26db0644819c092e3eae0c69385caa5a7b07da0d956da81981'
#https://web.totalcoin.io/?api-key=6f936af551561fdf8eec708719e1e0fe12b9556b660a6d05a767dd12b242f5cbf4aa6b91a7a9cc26db0644819c092e3eae0c69385caa5a7b07da0d956da81981#/dashboard

print(payment_history_summ_dates(api_access_token).text)