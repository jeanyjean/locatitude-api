import connexion
import six

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
from openapi_server import util


def controller_get_covid19(date):  # noqa: E501
    """Returns the covid19 cases of a specific date

     # noqa: E501

    :param date: 
    :type date: str

    :rtype: List[Covid19]
    """
    return 'do some magic!'


def controller_get_covid19_trend():  # noqa: E501
    """Returns the covid19 trend

     # noqa: E501


    :rtype: List[CovidTrend]
    """
    return 'do some magic!'


def controller_get_lat_long(date):  # noqa: E501
    """Returns the latitude and longitude of a specific date

     # noqa: E501

    :param date: 
    :type date: str

    :rtype: List[LatLong]
    """
    date = util.deserialize_date(date)
    return 'do some magic!'


def controller_get_new_covid19_each_day():  # noqa: E501
    """Returns the new covid cases of each day

     # noqa: E501


    :rtype: List[NewCovidEachDay]
    """
    return 'do some magic!'


def controller_get_pm(date):  # noqa: E501
    """Returns the PM2.5 of a specific date

     # noqa: E501

    :param date: 
    :type date: str

    :rtype: List[PM25]
    """
    date = util.deserialize_date(date)
    return 'do some magic!'


def controller_get_pm_each_day():  # noqa: E501
    """Returns the PM2.5 of each day

     # noqa: E501


    :rtype: List[PM25]
    """
    return 'do some magic!'


def controller_get_pm_trend():  # noqa: E501
    """Returns the PM2.5 trend

     # noqa: E501


    :rtype: List[PmTrend]
    """
    return 'do some magic!'


def controller_get_population(province):  # noqa: E501
    """Returns the population of a province

     # noqa: E501

    :param province: 
    :type province: str

    :rtype: List[Population]
    """
    return 'do some magic!'


def controller_get_province(date):  # noqa: E501
    """Returns the province of a specific date

     # noqa: E501

    :param date: 
    :type date: str

    :rtype: List[Province]
    """
    date = util.deserialize_date(date)
    return 'do some magic!'


def controller_get_provinces_population():  # noqa: E501
    """Returns the population of all the provinces

     # noqa: E501


    :rtype: List[Population]
    """
    return 'do some magic!'


def controller_get_show_all():  # noqa: E501
    """Returns all the information of each day

     # noqa: E501


    :rtype: List[AllDetails]
    """
    return 'do some magic!'


def controller_get_sum_covid19():  # noqa: E501
    """Returns the sum of the new covid cases in each province.

     # noqa: E501


    :rtype: List[SumCovid]
    """
    return 'do some magic!'
