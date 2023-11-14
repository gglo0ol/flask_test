from datetime import datetime as DT
import random
import json
from datetime import timedelta

class Random_data:

    _NAME = ['service_1', 'service_2', 'service_3', 'service_4', 'service_5', 'service_6', 'service_7', 'service_8', 'service_9', 'service_10']
    _STATUS = ['work', 'doesn\'t work', 'unstable']
    _DESCRIPTION = "it\'s string with description of service"
    _PATTERN = "%Y-%m-%d %H:%M"
    _START_TIME = DT.strptime('2022-01-01 00:00', _PATTERN)
    _END_TIME = DT.now()

    def __init__(self):
        self._name = random.choice(self._NAME)
        self._date = self.get_random_date().strftime(self._PATTERN)
        self._status = random.choice(self._STATUS)
        self._description = self._DESCRIPTION

    def __str__(self):
        result = {'name': self._name, 'date': self._date, 'status': self._status, 'description': self._description}
        return f'{result}'

    @property
    def name(self):
        return self._name

    @property
    def date(self):
        return self._date

    @property
    def status(self):
        return self._status

    @property
    def description(self):
        return self._description

    def get_random_date(self):
        '''Return random date and time from START_TIME to today'''
        delta = self._END_TIME - self._START_TIME
        random_date = self._START_TIME + timedelta(days=random.randint(0, delta.days - 1), seconds=random.randint(0, 3600 * 24))
        return random_date

    def get_json(self):
        result = {'name': self._name, 'date': self._date, 'status': self._status, 'description': self._description}
        data = json.dumps(result)
        return data

