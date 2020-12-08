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


token = chatRoomApi.get_token()

while 1:
    time.sleep(5)
    not_processed_commands = chatRoomApi.get_commands(token)

    for entry in not_processed_commands:
        command_regex = r'\/(.*)=(.*)'
        matches = re.search(command_regex, entry['content'])

        if matches is not None:
            command = matches.group(1)
            argument = matches.group(2)

            if command == 'stock':
                stock_response = requests.request("GET", stock_query_url.format(stock_code=argument))
                stock_information = stock_response.text.split('\n')[1].split(',')
                company = stock_information[0]
                close_price = stock_information[6]
                message_to_post = '{company} quote is ${close_price} per share'\
                    .format(company=company, close_price=close_price)

                q.put(message_to_post)
