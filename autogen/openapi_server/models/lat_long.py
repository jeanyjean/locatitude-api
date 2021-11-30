# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class LatLong(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, time_stamp=None, lat=None, long=None):  # noqa: E501
        """LatLong - a model defined in OpenAPI

        :param time_stamp: The time_stamp of this LatLong.  # noqa: E501
        :type time_stamp: str
        :param lat: The lat of this LatLong.  # noqa: E501
        :type lat: float
        :param long: The long of this LatLong.  # noqa: E501
        :type long: float
        """
        self.openapi_types = {
            'time_stamp': str,
            'lat': float,
            'long': float
        }

        self.attribute_map = {
            'time_stamp': 'timeStamp',
            'lat': 'lat',
            'long': 'long'
        }

        self._time_stamp = time_stamp
        self._lat = lat
        self._long = long

    @classmethod
    def from_dict(cls, dikt) -> 'LatLong':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LatLong of this LatLong.  # noqa: E501
        :rtype: LatLong
        """
        return util.deserialize_model(dikt, cls)

    @property
    def time_stamp(self):
        """Gets the time_stamp of this LatLong.


        :return: The time_stamp of this LatLong.
        :rtype: str
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this LatLong.


        :param time_stamp: The time_stamp of this LatLong.
        :type time_stamp: str
        """

        self._time_stamp = time_stamp

    @property
    def lat(self):
        """Gets the lat of this LatLong.


        :return: The lat of this LatLong.
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """Sets the lat of this LatLong.


        :param lat: The lat of this LatLong.
        :type lat: float
        """

        self._lat = lat

    @property
    def long(self):
        """Gets the long of this LatLong.


        :return: The long of this LatLong.
        :rtype: float
        """
        return self._long

    @long.setter
    def long(self, long):
        """Sets the long of this LatLong.


        :param long: The long of this LatLong.
        :type long: float
        """

        self._long = long
