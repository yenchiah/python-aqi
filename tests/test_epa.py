# -*- coding: utf-8 -*-

import unittest

from aqi.algos.epa import AQI
from aqi.constants import (POLLUTANT_PM25, POLLUTANT_PM10,
                          POLLUTANT_O3_8H, POLLUTANT_O3_1H,
                          POLLUTANT_CO, POLLUTANT_SO2, POLLUTANT_NO2)


class TestEPA(unittest.TestCase):
    """
    Test the EPA algorithm based on examples from the EPA official doc.
    """

    def test_O3(self):
        """Test Ozone AQI"""
        myaqi = AQI()
        self.assertEqual(
            myaqi.iaqi(POLLUTANT_O3_8H, '0.08753333'),
            129)
        self.assertEqual(
            myaqi.iaqi(POLLUTANT_O3_1H, '0.162'),
            147)
        self.assertEqual(
            myaqi.iaqi(POLLUTANT_O3_8H, '0.141'),
            211)

    def test_O3_PM25_CO(self):
        """Test O3, PM2.5 and CO AQI"""
        myaqi = AQI()
        self.assertEqual(
            myaqi.aqi([
                (POLLUTANT_O3_8H, '0.077'),
                (POLLUTANT_PM25, '40.9'),
                (POLLUTANT_CO, '8.4')
            ]),
            104)

    def test_blank_bp(self):
        """Test blank breakpoints"""
        myaqi = AQI()
        self.assertEqual(
            myaqi.iaqi(POLLUTANT_O3_8H, '0.087'),
            129)
