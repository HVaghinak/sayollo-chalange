import redis
from enum import Enum


class RedisSection(Enum):
    REQUESTS = 'requests'
    IMPRESSIONS = 'impressions'


class RedisSectionField(Enum):
    USERNAME = 'username'
    SDK_VERSION = 'sdk_version'


class RedisClient:
    _client = None

    def __init__(self):
        # TODO Read Redis credentials from Environment
        self._client = redis.Redis(host='redis', port=6379, db=0)

    def increment(self, section: RedisSection, field: RedisSectionField, value: str):
        """
        The stored key will be the combination of: section:field:value
        """
        self._client.incr(f"{section}:{field}:{value}")
