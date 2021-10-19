# Import/Export Design Pattern

This design pattern is used when you want to export a list of objects into a CSV file and import a CSV 
file to create a list of objects.


The design pattern has several pieces that should be built as stepping stones using test-driven development.
Each step is shown by presenting code that demonstrates the pattern.


## Table App

Create a new app for table code

    $ python manage.py startapp table

config/settings.py

    INSTALLED_APPS = [  ..., 'table', ]



## Executable Django Command

Run Custom Commands

    $ python manage.py quick_test

```python
    from django.core.management.base import BaseCommand, no_translations

    from table.table import read_csv_file


    class Command(BaseCommand):

        def handle(self, *args, **options):
            print("Quick Test")

            path = 'Documents/objects.csv'
            print(read_csv_file(path))
```



## CSV Reader
Read a file and convert into a table (list of rows)

```python
def read_csv_file(path):
    with open(path) as f:
        return [row for row in reader(f)]
```



## CSV Writer
Write a table (list of rows) into a CSV file.   Each row is a list
of values.

```python
def export_table(model):
    records = [o.values() for o in model.objects.all()]
    write_csv_file('Documents/objects.csv', records)
```


