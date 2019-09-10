import functools
from channels.handler import AsgiRequest
from django.conf import settings
from openedx.core.djangoapps.safe_sessions.middleware import SafeCookieData


def decode_safe_cookie_data_decorator(func):
    """

    """
    @functools.wraps(func)
    def inner(message, *args, **kwargs):
        message = decode_safe_cookie_data(message, *args, **kwargs)
        return func(message, *args, **kwargs)
    return inner


def decode_safe_cookie_data(message, *args, **kwargs):
    """
    """
    try:
        # We want to parse the WebSocket (or similar HTTP-lite) message
        # to get cookies and GET, but we need to add in a few things that
        # might not have been there.
        if "method" not in message.content:
            message.content['method'] = "FAKE"
        request = AsgiRequest(message)
    except Exception as e:
        raise ValueError("Cannot parse HTTP message - are you sure this is a HTTP consumer? %s" % e)
    session_key = request.COOKIES.get(settings.SESSION_COOKIE_NAME, None)
    if session_key:

        safe_cookie_data = SafeCookieData.parse(session_key)  # Step 1

        message.content['query_string'] = '{}={}'.format('session_key', safe_cookie_data.session_id)
    return message