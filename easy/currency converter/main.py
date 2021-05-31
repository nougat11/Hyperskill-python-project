import requests
import json
code1 = input()

rate = 0
cache = {}
while True:
    code2 = input()
    if code2 == '':
        break
    amount = int(input())

    pair = code1 + code2
    if code1+'usd' not in cache and code1 != 'usd':
        r = requests.get(f'http://www.floatrates.com/daily/{code1}.json')
        q = json.loads(r.text)

        cache[code1+'usd'] = q['usd']['rate']
        cache['usd' + code1] = q['usd']['inverseRate']
    if code1+'eur' not in cache and code1 != 'eur':
        r = requests.get(f'http://www.floatrates.com/daily/{code1}.json')
        q = json.loads(r.text)
        cache[code1+'eur'] = q['eur']['rate']
        cache['eur' + code1] = q['eur']['inverseRate']

    print("Checking the cache...")

    if pair not in cache:
        print("Sorry, but it is not in the cache!")
        r = requests.get(f'http://www.floatrates.com/daily/{code1}.json')
        q = json.loads(r.text)
        cache[pair] = q[code2.lower()]['rate']
        cache[code2+code1] = q[code2.lower()]['inverseRate']
        rate = q[code2.lower()]['rate']
    elif pair in cache:
        rate = cache[pair]
        print('Oh! It is in the cache!')
    print(f"You received {round(amount * rate, 2)} {code2}")
