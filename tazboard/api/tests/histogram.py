import os
import json

from unittest.mock import MagicMock, patch, Mock

from django.test import LiveServerTestCase
from elasticsearch import ConnectionError, RequestError

from tazboard.api.errors import ErrorCode
from tazboard.api.queries.constants import INTERVAL_10MINUTES

TEST_PATH = os.path.dirname(os.path.abspath(__file__))


class HistogramTestCase(LiveServerTestCase):

    def setUp(self):
        self.patcher = patch('tazboard.api.elastic_client.es')
        self.es_client = self.patcher.start()
        with open(os.path.join(TEST_PATH, 'mocks/histogram.json')) as mock_response:
            self.es_client.search = MagicMock(return_value=json.load(mock_response))

    def tearDown(self):
        self.patcher.stop()

    def test_unfiltered_histogram_response(self):
        response = self.client.get('/api/v1/histogram')
        data = response.json()
        self.assertIn('data', data)
        self.assertIn('total', data)
        self.assertGreater(data['total'], 0)
        self.assertEqual(response.status_code, 200)

    @patch('tazboard.api.views.get_histogram_query')
    def test_unfiltered_histogram_query_only_timeframe(self, get_histogram_query):
        self.client.get('/api/v1/histogram?min=now-24h&max=now')
        self.es_client.search.assert_called_once()
        get_histogram_query.assert_called_once()
        get_histogram_query.assert_called_with('now-24h', 'now', msid=None, interval=INTERVAL_10MINUTES)

    @patch('tazboard.api.views.get_histogram_query')
    def test_unfiltered_histogram_query_specify_msid(self, get_histogram_query):
        self.client.get('/api/v1/histogram?min=now-24h&max=now&msid=5555')
        self.es_client.search.assert_called_once()
        get_histogram_query.assert_called_once()
        get_histogram_query.assert_called_with('now-24h', 'now', msid='5555', interval=INTERVAL_10MINUTES)

    @patch('tazboard.api.views.get_histogram_query')
    def test_unfiltered_histogram_query_specify_interval(self, get_histogram_query):
        self.client.get('/api/v1/histogram?min=now-12h&max=now&interval=25m')
        self.es_client.search.assert_called_once()
        get_histogram_query.assert_called_once()
        get_histogram_query.assert_called_with('now-12h', 'now', msid=None, interval='25m')

    def test_expect_503_if_elastic_is_unavailable(self):
        self.es_client.search = Mock(side_effect=ConnectionError())
        response = self.client.get('/api/v1/histogram')
        self.assertEquals(response.status_code, 503)

    def test_expect_500_if_bad_elastic_query(self):
        self.es_client.search = Mock(side_effect=RequestError('kaboom', 'error', {}))
        response = self.client.get('/api/v1/histogram')
        self.assertEquals(response.status_code, 500)
