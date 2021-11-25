from requests import get

from .models import Test, Result


def clear_probe_history(probe_pk):
    Result.objects.filter(probe__pk=probe_pk).delete()


def execute_probe(probe):
    try:
        response = exec(probe.source)
    except:
        response = None

    if not response:
        status = f'Test Failed to execute:  {probe.name}'
        passed = False
    elif response != probe.expected:
        status = f'Test Produced Unexpected Results: {response}'
        passed = False
    else:
        status = f'Found Expected results'
        passed = True
    Result.create(probe=probe, output=status, passed=passed)


def launch_all_probes():
    for probe in Test.objects.all():
        execute_probe(probe)


def result_list(probe):
    return Result.objects.filter(probe=probe)
