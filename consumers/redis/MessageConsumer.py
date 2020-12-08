from ChatRoomApiManager import ChatRoomApiManager
from RedisQueue import RedisQueue
import time

time.sleep(1)

chatRoomApi = ChatRoomApiManager()
token = chatRoomApi.get_token()

q = RedisQueue('bot_response')


while 1:
    time.sleep(3)
    content = q.get()
    if content is None:
        continue
    chatRoomApi.post_message(token, content)
