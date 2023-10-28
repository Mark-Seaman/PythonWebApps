from pathlib import Path
from json import loads
from typing import Any, Dict
from django.template.loader import render_to_string
from markdown import markdown
import pandas as pd
from django.views.generic import TemplateView


def read_json(filename):
    path = Path(filename)
    if path.exists():
        return loads(path.read_text())
    return {}


def plan():
    milestone_markdown('milestones.md')
    milestone_html('milestones.html')


def milestone_markdown(path):
    data = milestone_data()
    markdown = render_to_string('plan.md', dict(milestones=data))
    Path(path).write_text(markdown)


def milestone_data():
    def role(x,y):
        t = f'{x}/{y}'
        task = tasks[t]
        role = task["role_name"]
        role = role[:role.index('-')]
        return [role, [task["deliverable"]]+task["details"]]
         
    def ms(x):
        return [ f"Milestone {int(x)+1} - {milestones[x]}", 
                [role(x,y) for y in range(4)]]

    print('# PLAN PROJECT')
    devplan = read_json('devplan.json')
    tasks = devplan['tasks']
    milestones = devplan['milestones']
    return [ms(x) for x in milestones]
     

def milestone_table():
    def details(x):
        text = '<ul>'
        for y in x:
            text += f"<li>{y}</li>"
        text += '</ul>'
        return text
    
    def roles(x):
        return [task_summary(role) for role in x]
    
    def task_summary(role):
        text = f'<strong>{role[0]}</strong><br>{role[1][0]}<br>{details(role[1][1:])}'
        print(text)
        return text
    
    data = milestone_data()
    return [[row[0]]+roles(row[1]) for row in data]


def milestone_html(path):
    table = milestone_table()
    df = pd.DataFrame(table, columns=["Milestone", "Requirements", 'Design', "Code", "Test"])
    df.to_html(path, index=False, escape=False)


class PlanView(TemplateView):
    template_name = 'planning_grid.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(table=milestone_table())
    
