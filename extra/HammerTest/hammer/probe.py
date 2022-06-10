from inspect import getmembers, isfunction
from os import listdir
from requests import get

from .models import Test, Result


def approve_result(result):
    probe = result.probe
    probe.expected = result.output
    probe.save()
    return execute_probe(probe)


def accept_results():
    for r in Result.objects.all():
        approve_result(r)
        # probe = r.probe
        # probe.expected = r.output
        # probe.save()
        # print(f'Accept Test Results: {probe.name}')
    Result.objects.all().delete()


def clear_probe_history(probe_pk=None):
    if probe_pk:
        Result.objects.filter(probe__pk=probe_pk).delete()
    else:
        Result.objects.all().delete()


def count_files(label, file_function):
    files = file_function()
    print(f'\nFiles in {label} - {len(files)}')
    for f in files:
        print(' '*4, f)


m = ''   # Needed for test_map()
all_probes = {}


def execute_probe(probe):

    def get_test_function(probe):
        global all_probes
        return all_probes[probe.source]

    try:
        # print(f'\nRun Test: {probe.name}')
        output = get_test_function(probe)()
        # print(f'OUTPUT:\n{response}')
        passed = output == probe.expected
    except:
        output = f'Test Failed to execute:  {probe.name}'
        passed = False

    return Result.create(probe=probe, output=output, passed=passed)


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

    global all_probes

    for module_name in module_list('test'):
        for f in test_functions(module_name):
            source = '.'.join(['test', module_name, f[0]])
            all_probes[f[0]] = f[1]


# def launch_all_probes():
#     for probe in Test.objects.all():
#         execute_probe(probe)


def result_list(probe):
    return Result.objects.filter(probe=probe)


def reset_tests():
    global all_probes
    Test.objects.all().delete()
    all_probes = {}
    register_tests()


def register_tests():
    find_tests()
    for f in all_probes:
        Test.create(name=f, source=f)
        # print(f'Register: {f}')


def run_tests():

    Result.objects.all().delete()
    for probe in Test.objects.all():
        execute_probe(probe)


def test_results():
    for r in Result.objects.all():
        print(f'\n\nTest Results: {r.probe.name}\n')
        print('    PASS' if r.passed else '    FAIL')
        print(f'\n    Expected:\n    {r.probe.expected}')
        print(f'\n    OUTPUT:\n    {r.output}')


register_tests()
