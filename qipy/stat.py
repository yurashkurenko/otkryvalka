import requests

# История платежей - сумма за диапазон дат
def payment_history_summ_dates(my_login, api_access_token, start_Date, end_Date):
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' + api_access_token
    parameters = {'startDate': start_Date,'endDate': end_Date}
    h = s.get('https://edge.qiwi.com/payment-history/v2/persons/' + my_login + '/payments/total', params = parameters)
    return h.json()

my_login=''
api_access_token=''
start_Date='2021-05-01T12:53:30+03:00'
end_Date='2021-05-31T12:53:30+03:00'
#start_Date='2021-03-01T00%3A00%3A00%2B03%3A00'
#end_Date='2021-03-31T11%3A44%3A15%2B03%3A00'
print(payment_history_summ_dates(my_login, api_access_token, start_Date, end_Date))
