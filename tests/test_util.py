from __future__ import absolute_import

import unittest
import datetime

from appannie import util


class TestUtil(unittest.TestCase):
    def test_round_to_day(self):
        day = datetime.datetime(2017, 3, 3, 1, 00, 00)
        expected_result = datetime.date(2017, 3, 3)
        result = util.round_to_day(day)
        self.assertEqual(result, expected_result)

    def test_to_day(self):
        expected_result = datetime.date(2017, 3, 3)

        result = util.to_day('2017-03-03')
        self.assertEqual(result, expected_result)

        result = util.to_day('2017-03-03 01:00:01', util.DATETIME_FORMAT)
        self.assertEqual(result, expected_result)

        result = util.to_day(datetime.datetime(2017, 3, 3, 1, 00, 1))
        self.assertEqual(result, expected_result)

        result = util.to_day(datetime.date(2017, 3, 3))
        self.assertEqual(result, expected_result)

        with self.assertRaises(ValueError):
            util.to_day(123456789)

        with self.assertRaises(ValueError):
            util.to_day('2017-03-03 invalid format')

    def test_collection_to_str(self):
        result = util.collection_to_str('US+GB')
        self.assertEqual(result, 'US+GB')

        result = util.collection_to_str(['US', 'GB'])
        self.assertEqual(result, 'US+GB')

        result = util.collection_to_str(['US', 'GB'], joinstr=',')
        self.assertEqual(result, 'US,GB')

        result = util.collection_to_str(('US', 'GB'))
        self.assertEqual(result, 'US+GB')
        result = util.collection_to_str({'US', 'GB'})
        self.assertTrue(result == 'US+GB' or result == 'GB+US')

    def test_format_request_data(self):
        data = {
            'device': 'iphone+ipad',
            'start_date': '2017-03-03',
            'end_date': datetime.date(2017, 3, 10),
            'date': None,
            'keywords': ['uber', 'netflix'],
            'countries': ['US', 'AU'],
        }
        expected = {
            'device': 'iphone+ipad',
            'start_date': '2017-03-03',
            'end_date': '2017-03-10',
            'keywords': 'uber,netflix',
            'countries': 'US+AU',
        }
        result = util.format_request_data(**data)
        self.assertEqual(result, expected)
