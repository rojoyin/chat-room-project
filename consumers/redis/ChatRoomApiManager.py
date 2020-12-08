import requests
import json


class ChatRoomApiManager(object):
    def __init__(self):
        self.api_base_url = 'http://app:8000'

    def get_token(self):
        bot_user = 'bot'
        bot_password = '123rest@'
        payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\n{user}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n{password}\r\n-----011000010111000001101001--\r\n" \
            .format(user=bot_user, password=bot_password)
        headers = {
            'Content-Type': "multipart/form-data",
            'content-type': "multipart/form-data; boundary=---011000010111000001101001"
        }
        auth_url = "{api_base_url}/auth/".format(api_base_url=self.api_base_url)
        response = requests.request("POST", auth_url, data=payload, headers=headers)
        return json.loads(response.text)['token']

    def post_message(self, token, content):
        messages_url = "{api_base_url}/api/chat/messages/".format(api_base_url=self.api_base_url)
        payload = {'room': 'default', 'content': content}
        headers = {
            'Authorization': 'Token {token}'.format(token=token)
        }
        requests.request("POST", messages_url, data=payload, headers=headers)
