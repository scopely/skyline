import unittest2 as unittest
from mock import Mock, patch
from time import time

import sys
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))) + '/src')
sys.path.insert(0, dirname(dirname(abspath(__file__))) + '/src/analyzer')

from graphite import Graphite

class TestGraphite(unittest.TestCase):

    def test_fetch_data(self):
        graphite = Graphite("sumSeries(stats.WithBuddies.Api.GameTurn.*.*.*.*)")
        ts = graphite.time_series("-24h")
        print ts


if __name__ == "__main__":
    unittest.main()
