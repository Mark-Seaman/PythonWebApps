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
    return dict(body=markdown(markdown_text), file=document, color='bg-primary text-light p-5', width='', link=link)


def document_data(document):
    return dict(documents=[document_card(document)])


def card_data(title="Random Card", body=None, color='bg-primary text-light', width='col-lg-12', link=None):
    if not body:
        body = lorem(400)
    html = markdown(body)
    return dict(title=title, header=title, body=html, color=color, width=width)


def cards_data():
    return [
        card_data(),
        card_data("Card Two",   lorem(50),  "bg-warning text-dark", 'col-lg-6'),
        card_data("Card Three", lorem(150), "bg-success text-light", 'col-lg-6'),
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


def table_data(path):
    return [row[: 5] for row in reader(open(path))]


def tabs_data():

    def options(i, tab, selected):
        data = tab
        if selected:
            data.update(dict(name=f'tab{i}', active='active', show='show', selected='true'))
        else:
            data.update(dict(name=f'tab{i}', active='', show='', selected='false'))
        return data

    def set_options(tabs):
        return [options(i, tab, i == 0) for i, tab in enumerate(tabs)]

    def create_pane_1():
        data = card_data(title="Cards", body='This is a display of **cards**')
        data['cards'] = cards_data()
        return data

    def create_pane_2():
        data = card_data(title="Doc Files", body='This is a display of **files**')
        data['cards'] = [document_card('Index')]
        return data

    def create_pane_3():
        data = card_data(title="Table", body='This is a display of **table**')
        data['tables'] = [table_data('Documents/lessons.csv')]
        return data

    def create_tabs():
        return [
            create_pane_1(),
            create_pane_2(),
            create_pane_3(),
        ]

    return set_options(create_tabs())


def super_data():
    return dict(document=document_data('README'),
                table=table_data('Documents/lessons.csv'),
                carousel=carousel_data(),
                tabs=tabs_data())
