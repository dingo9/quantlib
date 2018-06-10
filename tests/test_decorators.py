from datetime import datetime
import unittest
from quant.common.decorators import single_instance, method_dispatch


class DecoratorsTestCase(unittest.TestCase):
    def test_single_instance_for_class(self):
        @single_instance
        class A:
            pass

        a = A()
        b = A()
        self.assertTrue(a is b)

    def test_single_instance_for_function(self):
        @single_instance
        def func():
            return {}

        a = func()
        a['a'] = 1
        b = func()
        self.assertTrue(a is b)

    def test_method_dispatch(self):
        class A:
            @method_dispatch
            def func(self, arg):
                return None

            @func.register(str)
            def _(self, arg):
                return str

            @func.register(int)
            def _(self, arg):
                return int

        a = A()
        self.assertTrue(a.func(1.2) is None)
        self.assertTrue(a.func("") is str)
        self.assertTrue(a.func(10) is int)
