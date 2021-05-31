import requests
import json
code = input()
r = requests.get(f'http://www.floatrates.com/daily/{code}.json')
q = json.loads(r.text)
print(q['usd'])
print(q['eur'])
