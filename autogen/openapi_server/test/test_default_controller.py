# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.all_details import AllDetails  # noqa: E501
from openapi_server.models.covid19 import Covid19  # noqa: E501
from openapi_server.models.covid_trend import CovidTrend  # noqa: E501
from openapi_server.models.lat_long import LatLong  # noqa: E501
from openapi_server.models.new_covid_each_day import NewCovidEachDay  # noqa: E501
from openapi_server.models.pm25 import PM25  # noqa: E501
from openapi_server.models.pm_trend import PmTrend  # noqa: E501
from openapi_server.models.population import Population  # noqa: E501
from openapi_server.models.province import Province  # noqa: E501
from openapi_server.models.sum_covid import SumCovid  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_controller_get_covid19(self):
        """Test case for controller_get_covid19

        Returns the covid19 cases of a specific date
        """
        headers = { 
        }
        response = self.client.open(
            '/locatitude/covid/{date}'.format(date='date_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_covid19_trend(self):
        """Test case for controller_get_covid19_trend

        Returns the covid19 trend
        """
        headers = { 
        }
        response = self.client.open(
            '/locatitude/covid/trend/',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_lat_long(self):
        """Test case for controller_get_lat_long

        Returns the latitude and longitude of a specific date
        """
        headers = { 
        }
        response = self.client.open(
            '/locatitude/latlong/{date}'.format(date='2013-10-20'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_new_covid19_each_day(self):
        """Test case for controller_get_new_covid19_each_day

        Returns the new covid cases of each day
        """
        headers = { 
        }
        response = self.client.open(
            '/locatitude/covid/new/eachday/',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_pm(self):
        """Test case for controller_get_pm

        Returns the PM2.5 of a specific date
        """
        headers = { 
        }
        response = self.client.open(
            '/locatitude/pm/{date}'.format(date='2013-10-20'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_pm_each_day(self):
        """Test case for controller_get_pm_each_day

        Returns the PM2.5 of each day
        """
        headers = { 
        }
        response = self.client.open(
            '/locatitude/pm/eachday/',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_pm_trend(self):
        """Test case for controller_get_pm_trend

        Returns the PM2.5 trend
        """
        headers = { 
        }
        response = self.client.open(
            '/locatitude/pm/trend/',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_population(self):
        """Test case for controller_get_population

        Returns the population of a province
        """
        headers = { 
        }
        response = self.client.open(
            '/locatitude/population/{province}'.format(province='province_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_province(self):
        """Test case for controller_get_province

        Returns the province of a specific date
        """
        headers = { 
        }
        response = self.client.open(
            '/locatitude/province/{date}'.format(date='2013-10-20'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_provinces_population(self):
        """Test case for controller_get_provinces_population

        Returns the population of all the provinces
        """
        headers = { 
        }
        response = self.client.open(
            '/locatitude/population/allprovinces',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_show_all(self):
        """Test case for controller_get_show_all

        Returns all the information of each day
        """
        headers = { 
        }
        response = self.client.open(
            '/locatitude/showall/',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_sum_covid19(self):
        """Test case for controller_get_sum_covid19

        Returns the sum of the new covid cases in each province.
        """
        headers = { 
        }
        response = self.client.open(
            '/locatitude/covid/sum/',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
