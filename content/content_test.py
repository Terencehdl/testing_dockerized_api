import os
import requests

api_address = 'api'
api_port = 8000
log_path = '/app/logs/log.txt'

users = [{'username': 'alice', 'password': 'wonderland'}]

phrases = ['life is beautiful', 'that sucks']

for user in users:
    for version in ['v1', 'v2']:
        for phrase in phrases:
            r = requests.get(
                url=f'http://{api_address}:{api_port}/{version}/sentiment',
                params={
                    'username': user['username'], 'password': user['password'], 'sentence': phrase}
            )

            status_code = r.status_code
            score = r.text if status_code == 200 else 'N/A'

            sentiment = 'positive' if score == '1' else 'negative'
            expected_sentiment = 'positive' if phrase == 'life is beautiful' else 'negative'

            test_status = 'SUCCESS' if sentiment == expected_sentiment else 'FAILURE'

            output = f'''
============================
    Content test ({version})
============================

request done at "/{version}/sentiment"
| username="{user['username']}"
| password="{user['password']}"
| sentence="{phrase}"

expected sentiment = {expected_sentiment}
actual sentiment = {sentiment}
score = {score}

==>  {test_status}
'''

            print(output)

            if os.environ.get('LOG') == '1':
                with open(log_path, 'a') as file:
                    file.write(output)
