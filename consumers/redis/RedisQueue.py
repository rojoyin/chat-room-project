import redis


class RedisQueue(object):
    def __init__(self, name, namespace='queue', host='redis', **redis_kwargs):
        self.__db = redis.Redis(host, password='password',  **redis_kwargs)
        self.key = '%s:%s' % (namespace, name)

    def put(self, value):
        self.__db.rpush(self.key, value)

    def get(self):
        return self.__db.lpop(self.key)
