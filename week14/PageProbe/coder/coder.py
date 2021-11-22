from django.contrib.auth import get_user_model

from course.course import import_all_courses


def create_test_user():
    args = dict(username='seaman', email='me@here.com', password='secret')
    user = get_user_model().objects.filter(username='seaman')
    if user:
        user = user[0]
    else:
        user = get_user_model().objects.create_user(**args)
    return user, args


def quick_test():
    print("QUICK TEST")
    initialize_database()


def initialize_database():
    create_test_user()
    import_all_courses()
