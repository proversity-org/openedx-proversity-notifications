"""
Setup file for openedx_proversity_notifications Django plugin.
"""

from __future__ import print_function

import os
import re

from setuptools import setup


def get_version(*file_paths):
    """
    Extract the version string from the file at the given relative path fragments.
    """
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


VERSION = get_version('openedx_proversity_notifications', '__init__.py')


setup(
    name='openedx-proversity-notifications',
    version=VERSION,
    description='Plugin that implements django-channels in order to generate notifications on edx-platform.',
    author='andrey-canon',
    author_email='andrey.canon@edunext.co',
    packages=[
        'openedx_proversity_notifications'
    ],
    include_package_data=True,
    install_requires=[],
    zip_safe=False,
    entry_points={
        "lms.djangoapp": [
            'openedx_proversity_notifications = openedx_proversity_notifications.apps:OpenedxProversityNotificationsConfig',
        ],
    }
)
