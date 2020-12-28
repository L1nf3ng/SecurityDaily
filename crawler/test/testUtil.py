# -*- encoding:utf-8 -*-

import unittest
from crawler import dateTimeFormatter

class Temp:
    def __init__(self):
        self._prop = '2010-09-23'

    @dateTimeFormatter
    def setProp(self,prop=None):
        self._prop = prop


class MyTestCase(unittest.TestCase):
    def test_decrator(self):
        temp = Temp()
        # temp.setProp('2002年06月12日')
        temp.setProp(prop = '2002年06月12日')
        print(temp._prop)


if __name__ == '__main__':
    unittest.main()
