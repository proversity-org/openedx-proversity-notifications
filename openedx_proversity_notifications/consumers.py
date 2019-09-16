"""
Consumer file, includes all the consumers used by the plugin.
"""
import re

from channels.generic.websockets import WebsocketDemultiplexer

from openedx_proversity_notifications.auth import decode_safe_cookie_data
from openedx_proversity_notifications.binding import SubmissionsBinding, SubmissionsScoreBinding
from openedx_proversity_notifications.edxapp_wrapper.get_student_library import (
    get_course_enrollment,
)
from openedx_proversity_notifications.utils import is_course_staff


class OpenEdxSubmitionsDemultiplexer(WebsocketDemultiplexer):
    """
    Class that implements the necessary methods for the submissions notifications.
    """
    consumers = {
        'submissions': SubmissionsBinding.consumer,
        'submissions_score': SubmissionsScoreBinding.consumer,
    }
    http_user = True

    def get_handler(self, message, **kwargs):
        """
        Decode the session cookie value and replace it on the message.
        """
        message = decode_safe_cookie_data(message, **kwargs)
        return super(OpenEdxSubmitionsDemultiplexer, self).get_handler(message, **kwargs)

    def connect(self, message, **kwargs):
        """
        Validate if the user is authenticated and allow the web socket connection.
        """
        user = message.user

        if not user.is_authenticated():
            message.reply_channel.send({'close': True})

        super(OpenEdxSubmitionsDemultiplexer, self).connect(message, **kwargs)

    def connection_groups(self):
        """
        Generate the group list for the user connection.
        """
        user = self.message.user

        if not user.is_authenticated():
            return []

        groups = [
            'staff-{}'.format(re.sub(r'[\W]', '-', unicode(course.course_id)))
            for course in get_course_enrollment().objects.filter(user=user)
            if is_course_staff(user, course.course_id)
        ]

        groups.append('{}-updates'.format(user.username))

        return groups
