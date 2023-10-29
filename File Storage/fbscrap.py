import hashlib
import requests

app_id = '643157937997995'

combined_string = f'{app_id}|'
app_token = hashlib.md5(combined_string.encode()).hexdigest()

user_id = 'AnuvJain95'
url = f'https://graph.facebook.com/v12.0/{user_id}/feed'

params = {
    'access_token': app_token
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    for post in data.get('data', []):
        print(post.get('message', 'No message available'))
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
