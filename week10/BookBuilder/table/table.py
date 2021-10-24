from csv import reader, writer

from os.path import exists, isdir, dirname


def read_csv_file(path):
    assert exists(path)
    if exists(path):
        with open(path) as f:
            return [row for row in reader(f)]


def write_csv_file(path, table):
    assert(exists(dirname(path)))
    with open(path, 'w', newline='') as f:
        writer(f).writerows(table)
