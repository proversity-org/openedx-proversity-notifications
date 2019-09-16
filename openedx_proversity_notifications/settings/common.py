"""
Common Django settings for openedx_proversity_notifications project.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

from __future__ import unicode_literals

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'secret-key'


# Application definition

INSTALLED_APPS = []

ROOT_URLCONF = 'openedx_proversity_notifications.urls'


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_TZ = True


def plugin_settings(settings):
    """
    Set of plugin settings used by the Open Edx platform.
    More info: https://github.com/edx/edx-platform/blob/master/openedx/core/djangoapps/plugins/README.rst
    """
    settings.CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "asgiref.inmemory.ChannelLayer",
            "ROUTING": "openedx_proversity_notifications.routing.channel_routing",
        },
    }

    settings.INSTALLED_APPS.append(
        'channels'
    )

    settings.OPN_MODULESTORE = 'openedx_proversity_notifications.edxapp_wrapper.backends.modulestore_g_v1'
    settings.OPN_SAFE_SESSIONS = 'openedx_proversity_notifications.edxapp_wrapper.backends.safe_sessions_g_v1'
    settings.OPN_STUDENT_LIBRARY = 'openedx_proversity_notifications.edxapp_wrapper.backends.student_g_v1'
