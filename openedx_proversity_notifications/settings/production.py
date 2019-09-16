"""
Production Django settings for openedx_proversity_notifications project.
"""

from __future__ import unicode_literals


def plugin_settings(settings):
    """
    Set of plugin settings used by the Open Edx platform.
    More info: https://github.com/edx/edx-platform/blob/master/openedx/core/djangoapps/plugins/README.rst
    """
    settings.CHANNEL_LAYERS = getattr(settings, 'ENV_TOKENS', {}).get(
        'CHANNEL_LAYERS',
        settings.CHANNEL_LAYERS
    )
    settings.OPN_MODULESTORE = getattr(settings, 'ENV_TOKENS', {}).get(
        'OPN_MODULESTORE',
        settings.OPN_MODULESTORE
    )
    settings.OPN_SAFE_SESSIONS = getattr(settings, 'ENV_TOKENS', {}).get(
        'OPN_SAFE_SESSIONS',
        settings.OPN_SAFE_SESSIONS
    )
    settings.OPN_STUDENT_LIBRARY = getattr(settings, 'ENV_TOKENS', {}).get(
        'OPN_STUDENT_LIBRARY',
        settings.OPN_STUDENT_LIBRARY
    )
