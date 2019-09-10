import re

from django.db import models
from channels.channel import Group
from channels.binding.websockets import WebsocketBinding
from submissions.models import Score, StudentItem, Submission

from openedx_proversity_notifications.edxapp_wrapper.get_student_library import get_user_by_anonymous_id

class SubmissionsBinding(WebsocketBinding):

    model = Submission
    stream = 'submissions'
    fields = ['__all__']

    @classmethod
    def group_names(cls, instance):
        course_id = re.sub(r'[\W]', '-', instance.student_item.course_id)
        return ['staff-{}'.format(course_id)]

    def has_permission(self, user, action, pk):
        return False

    def send_messages(self, instance, group_names, action, **kwargs):
        """
        """
        if not group_names:
            return  # no need to serialize, bail.
        self.signal_kwargs = kwargs
        payload = self.serialize(instance, action)
        if payload == {}:
            return  # nothing to send, bail.

        payload['data'] = 'An assignment has been submitted.'

        assert self.stream is not None
        message = self.encode(self.stream, payload)
        for group_name in group_names:
            group = Group(group_name)
            group.send(message)

class SubmissionsScoreBinding(WebsocketBinding):

    model = Score
    stream = 'submissions_score'
    fields = ['__all__']

    @classmethod
    def group_names(cls, instance):
        student = get_user_by_anonymous_id(instance.student_item.student_id)
        return ['{}-updates'.format(student.username)]

    def has_permission(self, user, action, pk):
        return False

    def send_messages(self, instance, group_names, action, **kwargs):
        """
        """
        if not group_names:
            return  # no need to serialize, bail.
        self.signal_kwargs = kwargs
        payload = self.serialize(instance, action)
        if payload == {}:
            return  # nothing to send, bail.

        payload['data'] = 'Your assignment has been graded.'

        assert self.stream is not None
        message = self.encode(self.stream, payload)
        for group_name in group_names:
            group = Group(group_name)
            group.send(message)
