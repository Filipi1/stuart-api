from enum import Enum


class UserCacheKeysEnum(str, Enum):
    USER = "user:{token}"
