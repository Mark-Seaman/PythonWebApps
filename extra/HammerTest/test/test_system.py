from os.path import join
from os import walk


def test_system_source():
    files = len(recursive_files('.'))
    return f'System files: {files}'


def test_python_source():
    files = len(recursive_files('.', filetype='.py'))
    return f'Python files: {files}'


def test_templates_source():
    files = len(recursive_files('.', filetype='.html'))
    return f'Template files: {files}'


def test_test_source():
    files = len(recursive_files('test'))
    return f'Test files: {files}'


def recursive_files(d, filetype=None):
    matches = []
    for root, dirnames, filenames in walk(d):
        for filename in filenames:
            if not filetype or filename.endswith(filetype):
                matches.append(join(root, filename))
    return matches
