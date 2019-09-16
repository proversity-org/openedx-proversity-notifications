import functools

from channels.handler import AsgiRequest
from django.conf import settings

from openedx_proversity_notifications.edxapp_wrapper.get_safe_sessions import get_safe_cookie_data


def decode_safe_cookie_data_decorator(func):
    """
    Method that could be used as decorador in order to decode the cookie session value.
    """
    @functools.wraps(func)
    def inner(message, *args, **kwargs):
        message = decode_safe_cookie_data(message, *args, **kwargs)
        return func(message, *args, **kwargs)
    return inner


def decode_safe_cookie_data(message, *args, **kwargs):
    """
    Openedx safe session encodes the cookie session value, this method decodes
    the value and attachts it to the message.
    """
    try:
        # We want to parse the WebSocket (or similar HTTP-lite) message
        # to get cookies and GET, but we need to add in a few things that
        # might not have been there.
        if "method" not in message.content:
            message.content['method'] = "FAKE"
        request = AsgiRequest(message)
    except Exception as exception:
        raise ValueError("Cannot parse HTTP message - are you sure this is a HTTP consumer? %s" % exception)

    session_key = request.COOKIES.get(settings.SESSION_COOKIE_NAME, None)

    if session_key:
        safe_cookie_data = get_safe_cookie_data().parse(session_key)
        message.content['query_string'] = '{}={}'.format('session_key', safe_cookie_data.session_id)

    return message
