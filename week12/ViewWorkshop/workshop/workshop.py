from csv import reader
from markdown import markdown
from os.path import exists


def lorem(num_words):
    text = open('Documents/lorem.txt').read()
    return ' '.join(text.split(' ')[:num_words])
    

def accordion_data():

    def render_card_body(i):
        return f'<h2>Lessons (week {i})</h2><p>Lesson {i*3-2}</p><p>Lesson {i*3-1}</p><p>Lesson {i*3}</p>'

    def card_content(i, active):
        card = dict(id=i, title=f'Week {i+1}', body=render_card_body(i+1))
        if i == active:
            card['show'] = 'show'
            card['active'] = 'true'
        return card

    return [card_content(i, 0) for i in range(12)]


def card_data(title="Random Card", body=lorem(400), color='bg-primary', width='col-lg-12'):
    html = markdown(body)
    return dict(title=title, body=html, color=color, width=width)


def cards_data():
    return [
                card_data(),
                card_data("Card Two",   lorem(50),  "bg-warning", 'col-lg-4'),
                card_data("Card Three", lorem(150), "bg-success", 'col-lg-4'),
                card_data("Card Four",  lorem(20),  "bg-danger",  'col-lg-4'),
            ]


def carousel_data():
    return [["https://source.unsplash.com/random/1200x800?bear", "active"],
            ["https://source.unsplash.com/random/1200x800?forest", ''], 
            ["https://source.unsplash.com/random/1200x800?ocean"],
           ["https://source.unsplash.com/random/1200x800?flower"],
           ["https://images.unsplash.com/photo-1604932292784-ce6b48294afc"]]
    
    
def markdown_file_data(doc):
    doc = 'Documents/' + doc
    if not exists(doc):
        text = '# 404 is for Losers!'
    else:
        text = markdown(open(doc).read())
    title = f'Document - {doc}'
    return card_data(title, text, 'bg-success', 'col-lg-12') 


def table_data(path):
    return [row[:5] for row in reader(open(path))]


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
