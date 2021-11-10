from csv import reader
from markdown import markdown
from os.path import exists


def accordion_data():

    def create_card(i):
        return f'<h2>Lessons (week {i})</h2><p>Lesson {i*3-2}</p><p>Lesson {i*3-1}</p><p>Lesson {i*3}</p>'

    def card_content(i, active):
        card = card_data(f'Week {i+1}', create_card(i+1))
        if i == active:
            card.update(dict(id=i, collapsed='', show='show', aria='true'))
        else:
            card.update(dict(id=i, collapsed='collapsed', show='', aria='false'))
        return card

    return [card_content(i, 3) for i in range(12)]


def document_card(document):
    markdown_text = open(f'Documents/{document}.md').read()
    link = dict(href='Index', text='Doc Index')
    return dict(body=markdown(markdown_text), file=document, color='bg-success text-light', width='col-lg-6', link=link)


def document_data(document):
    return dict(documents=[document_card(document), document_card('Markdown')])


def card_data(title="Random Card", body=None, color='bg-primary text-light', width='col-lg-12', link=None):
    if not body:
        body = lorem(400)
    html = markdown(body)
    return dict(title=title, body=html, color=color, width=width)


def cards_data():
    return [
        card_data(),
        card_data("Card Two",   lorem(50),  "bg-warning text-dark", 'col-lg-4'),
        card_data("Card Three", lorem(150), "bg-success text-light", 'col-lg-8'),
        card_data("Card Four",  lorem(20),  "bg-danger text-light",  'col-lg-6'),
    ]


def carousel_data():
    return [
        dict(image_url="https://source.unsplash.com/random/1200x800?bear", label="Bear", active="active"),
        dict(image_url="https://source.unsplash.com/random/1200x800?forest", label="Forest"),
        dict(image_url="https://source.unsplash.com/random/1200x800?ocean", label="Ocean"),
        dict(image_url="https://source.unsplash.com/random/1200x800?flower", label="Flower"),
    ]


def lorem(num_words):
    text = open('Documents/lorem.txt').read()
    text = ' '.join(text.split(' ')[: num_words])
    return f'#### Lorem {num_words}\n\n' + text


def markdown_file_data(doc):
    doc = 'Documents/' + doc
    if not exists(doc):
        text = '# 404 is for Losers!'
    else:
        text = markdown(open(doc).read())
    title = f'Document - {doc}'
    return card_data(title, text, 'bg-success', 'col-lg-12')


def table_data(path):
    return [row[: 5] for row in reader(open(path))]


def tabs_data():

    def options(i, tab, selected):
        if selected:
            return dict(name=f'tab{i}', header=tab['title'], body=tab['body'],
                        active='active', show='show', selected='true')
        else:
            return dict(name=f'tab{i}', header=tab['title'], body=tab['body'],
                        active='', show='', selected='false')

    def set_options(tabs):
        return [options(i, tab, i == 0) for i, tab in enumerate(tabs)]

    return set_options(cards_data())


def super_data():
    return dict(card=markdown_file_data("README.md"),
                table=table_data('Documents/lessons.csv'),
                carousel=carousel_data(),
                tabs=tabs_data())
