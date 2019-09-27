"""
File that contains all the binding connections classes.
"""
import re
import logging

from channels.binding.websockets import WebsocketBinding
from submissions.models import Score, Submission

from openedx_proversity_notifications.edxapp_wrapper.get_student_library import get_user_by_anonymous_id
from openedx_proversity_notifications.utils import get_subsection_url_by_unit_id

logger = logging.getLogger(__name__)


class SubmissionsBinding(WebsocketBinding):
    """
    Class that allows to update changes over the Submission model.
    """
    model = Submission
    stream = 'submissions'
    fields = ['__all__']

    @classmethod
    def group_names(cls, instance):
        """
        Return a list with the group that will be allert about the submission change.
        """
        logger.info('********************Group names *********************')
        return ['staff-{}'.format(
            re.sub(r'[\W]', '-', instance.student_item.course_id),
        )]

    def has_permission(self, user, action, pk):
        """
        Do not allow any change over the model.
        """
        logger.info('********************has_permission*********************')
        return False

    def serialize_data(self, instance):
        """
        Return dict for the given Submission instance.
        """
        logger.info('********************serialize_data *********************')
        return {
            'title': 'An assignment has been submitted.',
            'message': 'The user {} has summitted an assignment'.format(
                get_user_by_anonymous_id(instance.student_item.student_id).username,
            ),
            'relative_url': get_subsection_url_by_unit_id(instance.student_item.item_id),
        }


class SubmissionsScoreBinding(WebsocketBinding):
    """
    Class that allows to update changes over the Score model.
    """

    model = Score
    stream = 'submissions_score'
    fields = ['__all__']

    @classmethod
    def group_names(cls, instance):
        """
        Return a list with the group that will be allert about the submission_score change.
        """
        logger.info('********************group_names 2*********************')
        return ['{}-updates'.format(
            get_user_by_anonymous_id(instance.student_item.student_id)
        )]

    def has_permission(self, user, action, pk):
        """
        Do not allow any change over the model.
        """
        logger.info('********************has_permission 2*********************')
        return False

    def serialize_data(self, instance):
        """
        Return dict for the given Score instance.
        """
        logger.info('********************serialize_data 2*********************')
        return {
            'title': 'Your assignment has been graded.',
            'message': 'Your assignment has been graded with {} points over {}'.format(
                instance.points_earned,
                instance.points_possible,
            ),
            'relative_url': get_subsection_url_by_unit_id(instance.student_item.item_id),
        }
