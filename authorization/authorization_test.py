import os
import requests

api_address = 'api'
api_port = 8000
log_path = '/app/logs/log.txt'

users = [
    {'username': 'alice', 'password': 'wonderland'},
    {'username': 'bob', 'password': 'builder'}
]

for user in users:
    for version in ['v1', 'v2']:
        sentence = 'Life is beautiful.' if user['username'] == 'alice' else 'That sucks.'
        r = requests.get(
            url=f'http://{api_address}:{api_port}/{version}/sentiment',
            params={'username': user['username'],
                    'password': user['password'], 'sentence': sentence}
        )

        status_code = r.status_code
        score = r.text if status_code == 200 else 'N/A'

        test_status = 'SUCCESS' if status_code == 200 else 'FAILURE'

        output = f'''
============================
    Authorization test ({version})
============================

request done at "/{version}/sentiment"
| username="{user['username']}"
| password="{user['password']}"
| sentence="{sentence}"

expected result = 200
actual result = {status_code}
score = {score}

==>  {test_status}
'''

        print(output)

        if os.environ.get('LOG') == '1':
            with open(log_path, 'a') as file:
                file.write(output)
