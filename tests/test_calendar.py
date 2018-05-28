from datetime import datetime
import unittest
from quant.utils.calendar import MonthlyCalendar


class MonthlyCalendarTestCase(unittest.TestCase):
    def test_last_day(self):
        calendar = MonthlyCalendar(2020, 2)
        self.assertEqual(calendar.last_day(), "2020-02-29")
        self.assertEqual(calendar.last_day(False), datetime(2020, 2, 29))

        calendar = MonthlyCalendar(2100, 2)
        self.assertEqual(calendar.last_day(), "2100-02-28")
        self.assertEqual(calendar.last_day(False), datetime(2100, 2, 28))

        calendar = MonthlyCalendar(2400, 2)
        self.assertEqual(calendar.last_day(), "2400-02-29")
        self.assertEqual(calendar.last_day(False), datetime(2400, 2, 29))

    def test_last_trading_day(self):
        self.assertEqual(MonthlyCalendar(2017, 12).last_trading_day(), "2017-12-29")
        self.assertEqual(MonthlyCalendar(2018, 4).last_trading_day(), "2018-04-27")

