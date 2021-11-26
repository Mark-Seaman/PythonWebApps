from test.test_system import test_python_source
from django.contrib.auth import get_user_model
from django.conf import settings
from inspect import getmembers, isfunction
from os import listdir

from hammer.models import Result, Test


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

    tests = register_tests()
    run_tests(tests)
    # accept_results()
    test_results()


def register_tests():
    # Test.objects.all().delete()
    tests = find_tests()
    for f in tests:
        Test.create(name=f, expected=None, source=f)
        print(f'Register: {f}')
    return tests


def run_tests(tests):
    # Result.objects.all().delete()
    for t in Test.objects.all():
        print(f'\nRun Test: {t.name}')
        output = tests[t.source]()
        print(f'OUTPUT:\n{output}')
        passed = output == t.expected
        Result.create(probe=t, output=output, passed=passed)


def test_results():
    for r in Result.objects.all():
        print(f'\n\nTest Results: {r.probe.name}')
        print('PASS' if r.passed else 'FAIL')
        print(f'\nExpected:\n{r.probe.expected}')
        print(f'\nOUTPUT:\n{r.output}')


def accept_results():
    for r in Result.objects.all():
        probe = r.probe
        probe.expected = r.output
        probe.save()
        print(f'Accept Test Results: {probe.name}')


m = ''   # Needed for test_map()


def find_tests():

    def module_list(directory):
        return [f.replace('.py', '') for f in listdir(directory) if f.startswith('test_')]

    def get_module(module_name):
        global m
        exec(f'import test.{module_name}; global m; m = test.{module_name}')
        return m

    def test_functions(module_name):
        module = get_module(module_name)
        functions = getmembers(module, isfunction)
        return [f for f in functions if f[0].startswith('test_')]

    test_names = {}
    for module_name in module_list('test'):
        for f in test_functions(module_name):
            source = '.'.join(['test', module_name, f[0]])
            test_names[source] = f[1]
    return test_names


def count_files(label, file_function):
    files = file_function()
    print(f'\nFiles in {label} - {len(files)}')
    # for f in files:
    #     print(' '*4, f)


def run_hammer_tests():
    pass
