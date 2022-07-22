from pathlib import Path
from json import loads


def read_json(filename):
    path = Path(filename)
    if path.exists():
        return loads(path.read_text())
    return {}


def plan():
    print('# PLAN PROJECT')
    devplan = read_json('devplan.json')
    tasks = devplan['tasks']
    milestones = devplan['milestones']

    print('## Milestones for Project\n')
    for x in milestones:

        m = f'{int(x)+1} - {milestones[x]}'
        print(f"* Milestone {m}")
        for y in range(4):
            t = f'{x}/{y}'

    print('\n\n## Goals by Milestone\n')
    for x in milestones:

        m = f'{int(x)+1} - { milestones[x]}'
        print(f"\nMilestone {m}\n")
        for y in range(4):
            t = f'{x}/{y}'
            task = tasks[t]
            print(f'    {task["role_name"]} - {task["deliverable"]}')

    print('\n\n## Detailed Deliverables\n')
    for x in milestones:

        m = f'{int(x)+1} - { milestones[x]}'
        print(f"\nMilestone {m}")
        for y in range(4):
            t = f'{x}/{y}'
            task = tasks[t]
            print(f'\n    {task["role_name"]} - {task["deliverable"]}')
            for d in task["details"]:
                print(f'        {d}')
