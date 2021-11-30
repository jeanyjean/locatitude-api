# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class CovidTrend(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, province=None, population=None, avg_covid=None):  # noqa: E501
        """CovidTrend - a model defined in OpenAPI

        :param province: The province of this CovidTrend.  # noqa: E501
        :type province: str
        :param population: The population of this CovidTrend.  # noqa: E501
        :type population: int
        :param avg_covid: The avg_covid of this CovidTrend.  # noqa: E501
        :type avg_covid: float
        """
        self.openapi_types = {
            'province': str,
            'population': int,
            'avg_covid': float
        }

        self.attribute_map = {
            'province': 'province',
            'population': 'population',
            'avg_covid': 'AvgCovid'
        }

        self._province = province
        self._population = population
        self._avg_covid = avg_covid

    @classmethod
    def from_dict(cls, dikt) -> 'CovidTrend':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CovidTrend of this CovidTrend.  # noqa: E501
        :rtype: CovidTrend
        """
        return util.deserialize_model(dikt, cls)

    @property
    def province(self):
        """Gets the province of this CovidTrend.


        :return: The province of this CovidTrend.
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        """Sets the province of this CovidTrend.


        :param province: The province of this CovidTrend.
        :type province: str
        """

        self._province = province

    @property
    def population(self):
        """Gets the population of this CovidTrend.


        :return: The population of this CovidTrend.
        :rtype: int
        """
        return self._population

    @population.setter
    def population(self, population):
        """Sets the population of this CovidTrend.


        :param population: The population of this CovidTrend.
        :type population: int
        """

        self._population = population

    @property
    def avg_covid(self):
        """Gets the avg_covid of this CovidTrend.


        :return: The avg_covid of this CovidTrend.
        :rtype: float
        """
        return self._avg_covid

    @avg_covid.setter
    def avg_covid(self, avg_covid):
        """Sets the avg_covid of this CovidTrend.


        :param avg_covid: The avg_covid of this CovidTrend.
        :type avg_covid: float
        """

        self._avg_covid = avg_covid