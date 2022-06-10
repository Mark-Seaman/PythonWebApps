from requests import get

from .models import Probe, Result


def clear_probe_history(probe_pk):
    Result.objects.filter(probe__pk=probe_pk).delete()


def execute_probe(probe):
    try:
        response = get(probe.page)
    except:
        response = None
    if not response:
        status = f'Status Code: Domain not found,  {probe.page}'
        passed = False
    elif response.status_code != 200:
        status = f'Status Code: {response.status_code}'
        passed = False
    elif probe.text not in response.text:
        status = f'Text not found: {probe.text}'
        passed = False
    else:
        status = f'Matched: {probe.text}'
        passed = True
    Result.create(probe=probe, output=status, passed=passed)


def launch_all_probes():
    for probe in Probe.objects.all():
        execute_probe(probe)


def result_list(probe):
    return Result.objects.filter(probe=probe)
