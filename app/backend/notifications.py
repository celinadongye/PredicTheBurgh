import nexmo
from time import gmtime, strftime

client = nexmo.Client(key='f3e0fd8b', secret='6EULCyQNBrwaK1j4')

def send_message(name, phone, pair, pair_name, rate, above_below):
    current_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    client.send_message({
        'from': 'ExchangeRates',
        'to': phone,
        'text': f'Hi {name}! Currency rate notification: {pair_name} rate has reached {above_below} {rate}: it is now {pair} ({current_time})',
    })

def check_if_send_notification(name, phone, rate, pair, pair_name, above_below):
    print(f'Rate: {rate}, pair rate: {pair}, {above_below}')
    if pair > rate and above_below == 'above':
        send_message(name, phone, pair, pair_name, rate, above_below)
        print('Above')
    elif pair < rate and above_below == 'below':
        send_message(name, phone, pair, pair_name, rate, above_below)
        print('Below')
