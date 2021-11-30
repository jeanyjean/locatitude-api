# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Covid19(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, time_stamp=None, newcovid=None, totalcovid=None):  # noqa: E501
        """Covid19 - a model defined in OpenAPI

        :param time_stamp: The time_stamp of this Covid19.  # noqa: E501
        :type time_stamp: str
        :param newcovid: The newcovid of this Covid19.  # noqa: E501
        :type newcovid: int
        :param totalcovid: The totalcovid of this Covid19.  # noqa: E501
        :type totalcovid: int
        """
        self.openapi_types = {
            'time_stamp': str,
            'newcovid': int,
            'totalcovid': int
        }

        self.attribute_map = {
            'time_stamp': 'timeStamp',
            'newcovid': 'newcovid',
            'totalcovid': 'totalcovid'
        }

        self._time_stamp = time_stamp
        self._newcovid = newcovid
        self._totalcovid = totalcovid

    @classmethod
    def from_dict(cls, dikt) -> 'Covid19':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Covid19 of this Covid19.  # noqa: E501
        :rtype: Covid19
        """
        return util.deserialize_model(dikt, cls)

    @property
    def time_stamp(self):
        """Gets the time_stamp of this Covid19.


        :return: The time_stamp of this Covid19.
        :rtype: str
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this Covid19.


        :param time_stamp: The time_stamp of this Covid19.
        :type time_stamp: str
        """

        self._time_stamp = time_stamp

    @property
    def newcovid(self):
        """Gets the newcovid of this Covid19.


        :return: The newcovid of this Covid19.
        :rtype: int
        """
        return self._newcovid

    @newcovid.setter
    def newcovid(self, newcovid):
        """Sets the newcovid of this Covid19.


        :param newcovid: The newcovid of this Covid19.
        :type newcovid: int
        """

        self._newcovid = newcovid

    @property
    def totalcovid(self):
        """Gets the totalcovid of this Covid19.


        :return: The totalcovid of this Covid19.
        :rtype: int
        """
        return self._totalcovid

    @totalcovid.setter
    def totalcovid(self, totalcovid):
        """Sets the totalcovid of this Covid19.


        :param totalcovid: The totalcovid of this Covid19.
        :type totalcovid: int
        """

        self._totalcovid = totalcovid