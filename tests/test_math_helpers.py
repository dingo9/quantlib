import unittest
import numpy as np
import pandas as pd
from quant.common.math_helpers import cal_mdd, exponential_decay_weight, Rolling


class MathTestCase(unittest.TestCase):
    def test_cal_mdd(self):
        # compound = True
        series = pd.Series([1.0, 1.1, 1.11, 1.04, 1.02, 1.08])
        mdd = cal_mdd(series)
        true_mdd = 1 - 1.02 / 1.11
        self.assertAlmostEqual(mdd, true_mdd)

        # compound = False
        mdd = cal_mdd(series, compound=False)
        true_mdd = 1.11 - 1.02
        self.assertAlmostEqual(mdd, true_mdd)

    def test_exponential_decay(self):
        # reverse = False
        weights = exponential_decay_weight(halflife=1, truncate_length=4, reverse=False)
        true_weights = np.array([1, 0.5, 0.25, 0.125])
        true_weights /= true_weights.sum()
        np.testing.assert_array_almost_equal(weights, true_weights)

        # reverse = True
        weights = exponential_decay_weight(halflife=1, truncate_length=4, reverse=True)
        true_weights = np.array([1, 0.5, 0.25, 0.125])
        true_weights /= true_weights.sum()
        true_weights = true_weights[::-1]
        np.testing.assert_array_almost_equal(weights, true_weights)

    def test_rolling(self):
        data = pd.DataFrame(np.random.randn(100, 3), index=pd.date_range("2000-01-01", periods=100), columns=["A", "B", "C"])
        data[data<-3] = np.nan
        rolling = Rolling(data, 10, min_periods=4)
        pd.testing.assert_frame_equal(rolling.mean(), data.rolling(10, min_periods=4).mean())
        pd.testing.assert_frame_equal(rolling.std(), data.rolling(10, min_periods=4).std())
        pd.testing.assert_frame_equal(rolling.sum(), data.rolling(10, min_periods=4).sum())
        pd.testing.assert_frame_equal(rolling.max(), data.rolling(10, min_periods=4).max())
        pd.testing.assert_frame_equal(rolling.min(), data.rolling(10, min_periods=4).min())

