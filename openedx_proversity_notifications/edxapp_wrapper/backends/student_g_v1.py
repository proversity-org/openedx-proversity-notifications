""" Backend abstraction """
from student.auth import user_has_role
from student.roles import CourseStaffRole
from student.models import CourseAccessRole, CourseEnrollment, UserProfile, user_by_anonymous_id


def user_has_role_backend(*args, **kwargs):
    """ Real backend to get user_has_role method. """
    return user_has_role(*args, **kwargs)


def course_staff_role_backend(*args, **kwargs):
    """ Real backend to get course staff role. """
    return CourseStaffRole(*args, **kwargs)


def course_access_role():
    """ Returns CourseAccessRole model. """
    return CourseAccessRole


def user_profile():
    """ Returns UserProfile model. """
    return UserProfile


def course_enrollment():
    """ Returns CourseEnrollment model. """
    return CourseEnrollment


def get_user_by_anonymous_id(*args, **kwargs):
    """ Returns the user_by_anonymous_id method. """
    return user_by_anonymous_id(*args, **kwargs)
