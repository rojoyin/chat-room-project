# Authentication
import requests
import json
import time
import re
from RedisQueue import RedisQueue

time.sleep(5)

api_base_url = 'http://app'
stock_query_url = 'https://stooq.com/q/l/?s={stock_code}&f=sd2t2ohlcv&h&e=csv'

q = RedisQueue('bot_response')

auth_url = "{api_base_url}:8000/auth/".format(api_base_url=api_base_url)
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

while 1:
    time.sleep(5)
    # Recover messages
    messages_url = "{api_base_url}:8000/api/chat/messages/".format(api_base_url=api_base_url)
    querystring = {"chat_room": "default"}
    headers = {'Authorization': 'Token {token}'.format(token=token)}
    response = requests.request("GET", messages_url, data=payload, headers=headers, params=querystring)
    not_processed_commands = [message for message in json.loads(response.text) if not message['processed_by_bot']
                              and message['content'].startswith('/')]

    for entry in not_processed_commands:
        command_regex = r'\/(.*)=(.*)'
        matches = re.search(command_regex, entry['content'])
        if matches is not None:
            command = matches.group(1)
            argument = matches.group(2)

            if command == 'stock':
                stock_response = requests.request("GET", stock_query_url.format(stock_code=argument),
                                                  params=querystring)
                stock_information = stock_response.text.split('\n')[1].split(',')
                company = stock_information[0]
                close_price = stock_information[6]
                message_to_post = '{company} quote is ${close_price} per share'\
                    .format(company=company, close_price=close_price)

                q.put(message_to_post)

                recovered_message = q.get()

                print('>>>>>>>>>>>>>>', recovered_message)
