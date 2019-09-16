""" Backend abstraction """
from openedx.core.djangoapps.safe_sessions.middleware import SafeCookieData


def get_safe_cookie_data_backend(*args, **kwargs):  # pylint: disable=unused-argument
    """ Real backend to get SafeCookieData"""
    return SafeCookieData
