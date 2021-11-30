# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class PmTrend(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, province=None, population=None, avg_pm=None):  # noqa: E501
        """PmTrend - a model defined in OpenAPI

        :param province: The province of this PmTrend.  # noqa: E501
        :type province: str
        :param population: The population of this PmTrend.  # noqa: E501
        :type population: int
        :param avg_pm: The avg_pm of this PmTrend.  # noqa: E501
        :type avg_pm: float
        """
        self.openapi_types = {
            'province': str,
            'population': int,
            'avg_pm': float
        }

        self.attribute_map = {
            'province': 'province',
            'population': 'population',
            'avg_pm': 'AvgPM'
        }

        self._province = province
        self._population = population
        self._avg_pm = avg_pm

    @classmethod
    def from_dict(cls, dikt) -> 'PmTrend':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PmTrend of this PmTrend.  # noqa: E501
        :rtype: PmTrend
        """
        return util.deserialize_model(dikt, cls)

    @property
    def province(self):
        """Gets the province of this PmTrend.


        :return: The province of this PmTrend.
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        """Sets the province of this PmTrend.


        :param province: The province of this PmTrend.
        :type province: str
        """

        self._province = province

    @property
    def population(self):
        """Gets the population of this PmTrend.


        :return: The population of this PmTrend.
        :rtype: int
        """
        return self._population

    @population.setter
    def population(self, population):
        """Sets the population of this PmTrend.


        :param population: The population of this PmTrend.
        :type population: int
        """

        self._population = population

    @property
    def avg_pm(self):
        """Gets the avg_pm of this PmTrend.


        :return: The avg_pm of this PmTrend.
        :rtype: float
        """
        return self._avg_pm

    @avg_pm.setter
    def avg_pm(self, avg_pm):
        """Sets the avg_pm of this PmTrend.


        :param avg_pm: The avg_pm of this PmTrend.
        :type avg_pm: float
        """

        self._avg_pm = avg_pm
