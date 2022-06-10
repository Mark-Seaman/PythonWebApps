from markdown import markdown

from os.path import exists


def document_body(text, image_path=None):
    if image_path:
        text = fix_images(text, image_path)
    return text_join(text_lines(text))


def document_html(text):
    return markdown(text)


def document_title(path):
    if not exists(path):
        return 'Document not found, ' + path
    return text_lines(no_blank_lines(read_file(path)))[0]


def fix_images(text, image_path):
    return text.replace('](img/', '](%s/' % image_path)


def text_join(text):
    return '\n'.join(text)


def text_lines(text):
    return text.split('\n')


def no_blank_lines(text):
    text = text_lines(text)
    text = [x for x in text if x.strip() != '']
    text = text_join(text)
    return text


def read_file(path):
    try:
        return open(path).read()
    except:
        return f'Found bad document: {path}'
