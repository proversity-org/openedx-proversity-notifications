"""
"""
import re

from channels.generic.websockets import WebsocketDemultiplexer

from openedx_proversity_notifications.auth import decode_safe_cookie_data, decode_safe_cookie_data_decorator
from openedx_proversity_notifications.binding import SubmissionsBinding, SubmissionsScoreBinding
from openedx_proversity_notifications.edxapp_wrapper.get_student_library import(
    get_course_enrollment,
)


class OpenEdxSubmitionsDemultiplexer(WebsocketDemultiplexer):
    """
    """
    consumers = {
        'submissions': SubmissionsBinding.consumer,
        'submissions_score': SubmissionsScoreBinding.consumer,
    }
    http_user = True

    def get_handler(self, message, **kwargs):
        """
        """
        message = decode_safe_cookie_data(message, **kwargs)
        return super(OpenEdxSubmitionsDemultiplexer, self).get_handler(message, **kwargs)

    def connect(self, message, **kwargs):
        """
        """
        user = message.user

        if not user.is_authenticated():
            message.reply_channel.send({'close': True})

        super(OpenEdxSubmitionsDemultiplexer, self).connect(message, **kwargs)

    def connection_groups(self):
        """
        """
        user = self.message.user

        if not user.is_authenticated():
            return []

        if user.is_staff:
            course_enrollments = get_course_enrollment().objects.filter(user=user)
            return [
                'staff-{}'.format(re.sub(r'[\W]', '-', unicode(course.course_id)))
                for course in course_enrollments
            ]

        return ['{}-updates'.format(user.username)]
