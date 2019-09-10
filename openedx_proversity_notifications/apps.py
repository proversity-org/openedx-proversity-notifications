"""
App configuration for openedx_proversity_notifications.
"""

from __future__ import unicode_literals

from django.apps import AppConfig


class OpenedxProversityNotificationsConfig(AppConfig):
    """
    Plugin that implements django-channels in order to generate notifications on edx-platform. configuration.
    """
    name = 'openedx_proversity_notifications'
    verbose_name = 'Plugin that implements django-channels in order to generate notifications on edx-platform.'

    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': 'openedx-proversity-notifications',
                'regex': r'^openedx-proversity-notifications/',
                'relative_path': 'urls',
            },
        },
        'settings_config': {
            'lms.djangoapp': {
                'common': {'relative_path': 'settings.common'},
                'test': {'relative_path': 'settings.test'},
                'aws': {'relative_path': 'settings.aws'},
                'production': {'relative_path': 'settings.production'},
            },
            'cms.djangoapp': {
                'common': {'relative_path': 'settings.common'},
                'test': {'relative_path': 'settings.test'},
                'aws': {'relative_path': 'settings.aws'},
                'production': {'relative_path': 'settings.production'},
            },
        }
    }
