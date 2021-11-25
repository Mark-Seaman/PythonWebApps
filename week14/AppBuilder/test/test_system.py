from os.path import join
from os import walk


def test_system_source():
    print(recursive_files('..'))


def recursive_files(d):
    matches = []
    for root, dirnames, filenames in walk(d):
        for filename in filenames:
            path = join(root, filename)
            matches.append(path)
    return matches
