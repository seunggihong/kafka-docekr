import urllib.request
import json
import time
from kafka import KafkaProducer


def call_bitcoin(url, symbol='BTC'):
    response = urllib.request.urlopen(url)
    response_message = response.read().decode('utf8')

    jsonData = json.loads(response_message)
    coin_price = 0
    coin_ath_date = ''

    for data in jsonData:
        if data.get('symbol') == symbol:
            coin_price = data.get('quotes').get('KRW').get('price')
            coin_ath_date = data.get('quotes').get('KRW').get('ath_date')

    return coin_price, coin_ath_date


if __name__ == '__main__':
    url = 'https://api.coinpaprika.com/v1/tickers?quotes=KRW'

    topic_name = 'bitcoin'
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    start = time.time()
    print('[begin] start sending message from producer')
    try:
        while (True):
            price, ath_date = call_bitcoin(url)
            print('sending message...')
            data = f'bitcoin price : {price}, bitcoin ath date : {ath_date}'
            producer.send(
                topic_name, data.encode('utf-8'))
            producer.flush()
            time.sleep(3)
    except KeyboardInterrupt:
        print('[end] time taken', time.time() - start)
        pass
