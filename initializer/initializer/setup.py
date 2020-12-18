import requests
import json


# Create bot user for testing
print('::::::::::::::::::::::::::INICIAL:::::::::::::::')
url = "http://app:8000/api/user/create/"

payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\nbot\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n123rest@\r\n-----011000010111000001101001--\r\n"
headers = {
    'Content-Type': "multipart/form-data",
    'content-type': "multipart/form-data; boundary=---011000010111000001101001"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

# get token
bot_user = 'bot'
bot_password = '123rest@'
payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\n{user}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n{password}\r\n-----011000010111000001101001--\r\n" \
    .format(user=bot_user, password=bot_password)
headers = {
    'Content-Type': "multipart/form-data",
    'content-type': "multipart/form-data; boundary=---011000010111000001101001"
}
auth_url = "http://app:8000/auth/"
response = requests.request("POST", auth_url, data=payload, headers=headers)
token = json.loads(response.text)['token']

# Create default chatroom
url = "http://app:8000/api/chat/room/"

payload = "{\n\t\"name\": \"default\"\n}\n"
headers = {
    'Content-Type': "application/json",
    'Authorization': "Token {token}".format(token=token)
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
