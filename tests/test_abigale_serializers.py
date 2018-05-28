import unittest
import pandas as pd
from quant.abigale.serializers import DataFrameSerializer


class SerializerTestCase(unittest.TestCase):
    def test_dataframe_serializer(self):
        data = pd.DataFrame(
            [[1.0, 2.0], [-3.0, -1.0], [3.0, -1.2]],
            columns=["A", "B"],
            index=pd.to_datetime(["2010-01-01", "2010-01-02", "2010-01-03"])
        )

        # to_json = False
        data_immediate = DataFrameSerializer.serialize(data, to_json=False)
        data_copy = DataFrameSerializer.unserialize(data_immediate)
        pd.testing.assert_frame_equal(data, data_copy, check_datetimelike_compat='equiv')

        # to_json = True
        data_immediate = DataFrameSerializer.serialize(data, to_json=True)
        data_copy = DataFrameSerializer.unserialize(data_immediate)
        pd.testing.assert_frame_equal(data, data_copy, check_datetimelike_compat='equiv')
