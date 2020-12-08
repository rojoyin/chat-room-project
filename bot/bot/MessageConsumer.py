# Authentication
import requests
import json,time

time.sleep(5)

api_base_url = 'http://app'

auth_url = "{api_base_url}:8000/auth/".format(api_base_url=api_base_url)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', auth_url)
token = ''

bot_user = 'bot'
bot_password = '123rest@'

payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\n{user}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n{password}\r\n-----011000010111000001101001--\r\n" \
    .format(user=bot_user, password=bot_password)

headers = {
    'Content-Type': "multipart/form-data",
    'content-type': "multipart/form-data; boundary=---011000010111000001101001"
    }

response = requests.request("POST", auth_url, data=payload, headers=headers)

# Save token
token = json.loads(response.text)['token']

# Recover messages
messages_url = "{api_base_url}:8000/api/chat/messages/".format(api_base_url=api_base_url)
querystring = {"chat_room": "default"}
payload = ""
headers = {'Authorization': 'Token {token}'.format(token=token)}
response = requests.request("GET", messages_url, data=payload, headers=headers, params=querystring)
not_processed_messages = [message for message in json.loads(response.text) if not message['processed_by_bot']]

print(len(not_processed_messages))


# Parse messages and make api calls for /stocks


# Save messages to database
