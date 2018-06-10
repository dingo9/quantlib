import sys
import pandas as pd
from pandas.tseries.offsets import CustomBusinessDay, BDay
from ...common import LOCALIZER, Logger


__all__ = ["TradingCalendar"]


class TradingCalendar:
    """中国金融市场交易日历"""
    def __init__(self):
        self.__holidays = None

    @staticmethod
    @LOCALIZER.wrap("holiday.h5", const_key="holiday")
    def get_holidays():
        from ...data import wind
        calendar = wind.get_wind_table("AShareCalendar", ["trade_days"])
        trading_days = set(pd.to_datetime(calendar.trade_days))
        all_days = pd.date_range(start=min(trading_days), end=max(trading_days))
        # 全部日期减去交易日再减双休日即得到节假日
        holidays = sorted(filter(lambda day: day.weekday() < 5, set(all_days) - trading_days))
        return pd.Series(holidays)

    @property
    def holidays(self):
        """
        中国A股市场休市日期

        type: List[str]
        """
        if not self.__holidays:
            self.__holidays = list(self.get_holidays())
        return self.__holidays

    @property
    def TradingDay(self):
        """根据获取的节假日信息生成pd.tseries.offsets.CustomBusinessDay对象"""
        try:
            return CustomBusinessDay(holidays=self.holidays)
        except:
            return BDay()

trading_calendar = TradingCalendar()
TDay = trading_calendar.TradingDay
"""交易日， pd.tseries.offset.CustomBusinessDay"""
