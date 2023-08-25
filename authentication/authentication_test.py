import os
import requests

api_address = 'api'
api_port = 8000
log_path = '/app/logs/log.txt'

users = [
    {'username': 'alice', 'password': 'wonderland'},
    {'username': 'bob', 'password': 'builder'},
    {'username': 'clementine', 'password': 'mandarine'}
]

for user in users:
    r = requests.get(
        url=f'http://{api_address}:{api_port}/permissions',
        params={'username': user['username'], 'password': user['password']}
    )

    expected_result = 200 if user['username'] in ['alice', 'bob'] else 403
    status_code = r.status_code

    test_status = 'SUCCESS' if status_code == expected_result else 'FAILURE'

    output = f'''
============================
    Authentication test
============================

request done at "/permissions"
| username="{user['username']}"
| password="{user['password']}"

expected result = {expected_result}
actual result = {status_code}

==>  {test_status}
'''

    print(output)

    if os.environ.get('LOG') == '1':
        with open(log_path, 'a') as file:
            file.write(output)
