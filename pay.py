import requests
import json
import time

def qiwi_amount(comment):
    api_access_token = ""
    my_login = ''
    amount = 0
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' + api_access_token
    s.headers['accept'] = 'application/json'
    parameters = {'rows': '10'}
    h = s.get(
        'https://edge.qiwi.com/payment-history/v2/persons/{0}/payments?rows=10&operation=IN&sources[0]=QW_RUB'.format(my_login),
        params=parameters)
    i = 0
    obj = json.loads(h.text)
    while i < 1:
        if(comment == obj['data'][i]['comment']):
            amount = obj['data'][i]['sum']['amount']
        i = i + 1
    return amount

def trans_id_gen():
    return int(float(time.time()*1000))

def send_money(amount, number):
    api_access_token = '791d6163a726eeb011b2820817473b8c'
    id = trans_id_gen()
    dict = {
        "id": str(id),
        "sum": {
            "amount": amount,
            "currency": "643"
        },
        "paymentMethod": {
            "type": "Account",
            "accountId": "643"
        },
        "comment": "test",
        "fields": {
            "account": "+" + str(number)
        }
    }
    payload = json.dumps(dict, separators=(',', ':'))
    r = requests.Session()
    r.headers['Content-Type'] = 'application/json'
    r.headers['Accept'] = 'application/json'
    r.headers['Authorization'] = 'Bearer ' + api_access_token
    rs = r.post("https://edge.qiwi.com/sinap/api/v2/terms/99/payments", data=payload)
    print(rs.text)

def test_send(amount, number):
    print("Amount: " + str(amount))
    print("Number: " + str(number))
