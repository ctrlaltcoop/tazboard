import os
from datetime import datetime

from django.utils.timezone import make_aware
from tazboard.core.settings import BASE_DIR


KEY_TIMEFRAME_AGGREGATION = "KEY_TIMEFRAME_AGGREGATION"
KEY_TREND_AGGREGATION = "KEY_TREND_AGGREGATION"
KEY_FINGERPRINT_AGGREGATION = "KEY_FINGERPRINT_AGGREGATION"
KEY_ARTICLE_COUNT_AGGREGATION = "KEY_ARTICLE_COUNT_AGGREGATION"
KEY_TIMESTAMP_AGGREGATION = "KEY_TIMESTAMP_AGGREGATION"
KEY_REFERRER_AGGREGATION = "KEY_REFERRER_AGGREGATION"
KEY_SUBJECTS_AGGREGATION = "KEY_SUBJECTS_AGGREGATION"
KEY_DEVICES_AGGREGATION = "KEY_DEVICES_AGGREGATION"
KEY_TOPLIST_AGGREGTAION = "KEY_TOPLIST_AGGREGTAION"
KEY_EXTRA_FIELDS_AGGREGATION = "KEY_EXTRA_FIELDS_AGGREGATION"
KEY_RANGES_AGGREGATION = "KEY_RANGES_AGGREGATION"
KEY_REFERRERTAGS_FINGERPRINT_AGGREGATION = "KEY_REFERRERTAGS_FINGERPRINT_AGGREGATION"
KEY_FIREPLACE_AGGREGATION = "KEY_FIREPLACE_AGGREGATION"

INTERVAL_10MINUTES = '10m'

MOCK_FAKE_NOW = make_aware(datetime(year=2020, month=8, day=20, hour=12, minute=00))
MOCK_CXML_PATH = os.path.join(BASE_DIR, '..', 'api', 'tests', 'mocks', 'c.xml')
