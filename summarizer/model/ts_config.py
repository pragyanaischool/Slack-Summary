"""Provide constants."""
import os

SUMMARY_INTERVALS = [{'days': 5, 'size': 2}, ]
TS_DEBUG = True
TS_LOG = 'ts_summ.log'
DEBUG = True
LOG_FILE = 'summary.log'
TEST_JSON = './data/test-events-elastic.json'
CHANNELS = ['api-test', 'calypso', 'games', 'happiness', 'hg', 'jetpack',
            'jetpackfuel', 'livechat', 'tickets', 'vip']
ROOT_PATH = os.getcwd()
CONFIG_PATH = os.path.join(ROOT_PATH, 'configs')
LOG_PATH = os.path.join(ROOT_PATH, 'logs')
TEMPORAL_VALUES = {'seconds', 'minutes', 'hours', 'days', 'weeks'}