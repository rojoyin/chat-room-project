# Authentication
import requests
import time
import re
from ChatRoomApiManager import ChatRoomApiManager
from RedisQueue import RedisQueue

time.sleep(5)

stock_query_url = 'https://stooq.com/q/l/?s={stock_code}&f=sd2t2ohlcv&h&e=csv'

q = RedisQueue('bot_response')

chatRoomApi = ChatRoomApiManager()
attended_commands = []

token = chatRoomApi.get_token()

while 1:
    time.sleep(10)
    not_processed_commands = chatRoomApi.get_commands(token)

    for entry in not_processed_commands:
        if entry['id'] in attended_commands:
            continue

        command_regex = r'\/(.*)=(.*)'
        matches = re.search(command_regex, entry['content'])

        if matches is None:
            continue

        command = matches.group(1)
        argument = matches.group(2)

        if command == 'stock':
            stock_response = requests.request("GET", stock_query_url.format(stock_code=argument))
            stock_information = stock_response.text.split('\n')[1].split(',')
            company = stock_information[0]
            close_price = stock_information[6]
            message_to_post = '{company} quote is ${price} per share'.format(company=company, price=close_price)
            attended_commands.append(entry['id'])
            q.put(message_to_post)
