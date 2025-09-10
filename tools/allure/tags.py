from enum import Enum

class AllureTag(str, Enum):
    USERS = 'USERS'
    COURSES = 'COURSES'
    FILES = 'FILES'
    EXERCISES = 'EXERCISES'
    AUTHENTICATION = 'AUTHENTICATION'
    REGRESSION = 'REGRESSION'