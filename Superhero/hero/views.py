from pathlib import Path
from django.views.generic import TemplateView

def hero_list():
    def hero_details(i, f):
        caption = ""
        strengths = ""
        weaknesses = ""
        if (i == 0):
            caption = "Black Widow"
            strengths = "Agility, Martial Arts, Espionage."
            weaknesses = "Supervillans."
        elif (i == 1):
            caption = "Captain America"
            strengths = "Frisbee, Jogging, History."
            weaknesses = "Pop Culture References."
        elif (i == 2):
            caption = "The Hulk"
            strengths = "Strength."
            weaknesses = "Brains."
        elif (i == 3):
            caption = "Iron Man"
            strengths = "Genius, Billionaire, Playboy, Philanthropist."
            weaknesses = "Humility."
        elif (i == 4):
            caption = "Spiderman"
            strengths = "Pizza Delivery."
            weaknesses = "Redheads."
        return dict(id=i, file=f, caption=caption, strengths=strengths, weaknesses=weaknesses)

    heroes = Path('static/images').iterdir()
    heroes = [hero_details(i, f) for i, f in enumerate(heroes)]
    return heroes

class HeroView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        i = kwargs['id']
        heroes = hero_list()
        p = heroes[i]
        print(p)
        return dict(hero=p)

class HeroListView(TemplateView):
    template_name = 'heroes.html'

    def get_context_data(self, **kwargs):
        return dict(heroes=hero_list())
