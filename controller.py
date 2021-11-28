import sys
from flask import abort
import pymysql as mysql
from config import OPENAPI_AUTOGEN_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME

sys.path.append(OPENAPI_AUTOGEN_DIR)
from openapi_server import models

db = mysql.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWD, db=DB_NAME)


def get_lat_long(date):
    cs = db.cursor()
    cs.execute(
        """
        SELECT timestamp, latitude, longitude
        FROM latlon
        WHERE DATE(timestamp) =%s
        """,
        [date],
    )
    result = [
        models.LatLong(timestamp, latitude, longitude)
        for timestamp, latitude, longitude in cs.fetchall()
    ]
    cs.close()
    return result


def get_pm(date):
    cs = db.cursor()
    cs.execute(
        """
        SELECT timestamp, pm25
        FROM pm25andprovince
        WHERE DATE(timestamp) =%s
        """,
        [date],
    )
    result = [models.PM25(timestamp, pm25) for timestamp, pm25 in cs.fetchall()]
    cs.close()
    return result


def get_province(date):
    cs = db.cursor()
    cs.execute(
        """
        SELECT timestamp, province
        FROM pm25andprovince
        WHERE DATE(timestamp) =%s
        """,
        [date],
    )
    result = [models.PM25(timestamp, province) for timestamp, province in cs.fetchall()]
    cs.close()
    return result


def get_population(province):
    cs = db.cursor()
    cs.execute(
        """
        SELECT province, population
        FROM population
        WHERE province =%s
        """,
        [province],
    )
    result = cs.fetchone()
    cs.close()
    if result:
        province, population = result
        return models.Population(province, population)
    else:
        abort(404)


def get_covid19(date):
    cs = db.cursor()
    cs.execute(
        """
        SELECT timestamp, newcovid, totalcovid
        FROM covid19
        WHERE DATE(timestamp) =%s
        """,
        [date],
    )
    result = [
        models.Covid19(timestamp, newcovid, totalcovid)
        for timestamp, newcovid, totalcovid in cs.fetchall()
    ]
    cs.close()
    return result


def get_provinces_population():
    cs = db.cursor()
    cs.execute(
        """
        SELECT province, population
        FROM population
        """
    )
    result = [
        models.ProvincePopulation(province, population)
        for province, population in cs.fetchall()
    ]
    cs.close()
    return result


def get_covid19_trend():
    cs = db.cursor()
    cs.execute(
        """
        SELECT p.province, population, newcovid
        FROM population p
        INNER JOIN covid19 c ON p.province=c.province
        """
    )
    result = [
        models.CovidTrend(province, population, newcovid)
        for province, population, newcovid in cs.fetchall()
    ]
    cs.close()
    return result


def get_sum_covid19():
    cs = db.cursor()
    cs.execute(
        """
        SELECT p.province, population, SUM(newcovid) as sum
        FROM population p
        INNER JOIN covid19 c ON p.province=c.province
        GROUP BY province, population
        """
    )
    result = [
        models.SumCovid(province, population, sum)
        for province, population, sum in cs.fetchall()
    ]
    cs.close()
    return result


def get_pm_trend():
    cs = db.cursor()
    cs.execute(
        """
        SELECT p.province, population, pm25
        FROM population p
        INNER JOIN pm25andprovince pm ON p.province=pm.province
        """
    )
    result = [
        models.PmTrend(province, population, pm25)
        for province, population, pm25 in cs.fetchall()
    ]
    cs.close()
    return result
