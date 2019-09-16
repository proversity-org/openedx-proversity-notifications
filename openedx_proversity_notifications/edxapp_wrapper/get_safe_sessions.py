""" Backend abstraction """
from importlib import import_module
from django.conf import settings


def get_safe_cookie_data(*args, **kwargs):
    """ Get modulestore """

    backend_function = settings.OPN_SAFE_SESSIONS
    backend = import_module(backend_function)

    return backend.get_safe_cookie_data_backend(*args, **kwargs)
