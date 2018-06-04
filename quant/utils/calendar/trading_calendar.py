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
        try:
            calendar = wind.get_wind_table("AShareCalendar", ["trade_days"])
        except Exception as e:
            Logger.fatal("Can't get trading calendar", e)
        trading_days = list(pd.to_datetime(calendar.trade_days).drop_duplicates().sort_values())
        all_days = pd.date_range(start=trading_days[0], end=trading_days[-1])
        holidays = sorted(filter(lambda day: day.weekday() < 5, set(all_days) - set(trading_days)))
        return pd.Series(holidays)

    @property
    def holidays(self):
        """
        中国期货市场休市日期

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
            return BDay

trading_calendar = TradingCalendar()
TDay = trading_calendar.TradingDay
"""交易日， pd.tseries.offset.CustomBusinessDay"""
