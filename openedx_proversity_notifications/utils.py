"""
Utils file.
"""
import logging

from django.core.urlresolvers import reverse
from opaque_keys.edx.locator import BlockUsageLocator

from openedx_proversity_notifications.edxapp_wrapper.get_modulestore import get_modulestore, item_not_found_error
from openedx_proversity_notifications.edxapp_wrapper.get_student_library import (
    get_course_staff_role,
    user_has_role,
)


LOG = logging.getLogger(__name__)


def get_subsection_url_by_unit_id(component_id):
    """
    Return the course section url for the given component_id.

    Args:
        unit_id = 'block-v1:edx+CS101+2019_T2+type@edx_sga+block@c4572ba7fd514f7fb38bc73aedd9522b'
    Returns:
        '/course-v1:edx+CS101+2019_T2/jump_to_id/d23a7a949dea4a9fa1af86930ff04020'

    """
    try:
        block = get_modulestore().get_item(BlockUsageLocator.from_string(component_id))
        block_parent = block.parent
    except item_not_found_error() as item_error:
        LOG.warn(
            'The component id %s is not valid, error: %s',
            component_id,
            item_error,
        )
        return ''

    return reverse('jump_to_id', args=[block_parent.course_key, block_parent.block_id])


def is_course_staff(user, course_key):
    """
    Return True if the user is the course staff
    else Returns False.

    Args:
        user: Dajngo user instance.
        course_key: CourseKey from opaque keys instance.
    Returns:
        True or False
    """
    return user_has_role(user, get_course_staff_role(course_key))
