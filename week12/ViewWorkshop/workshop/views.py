from .menu import load_menu, load_side_menu
from .workshop import accordion_data, card_data, cards_data, document_data, markdown_file_data, super_data, table_data, tabs_data
from django.views.generic import RedirectView, TemplateView
from os import listdir
from markdown import markdown
from django.views.generic import TemplateView


class HtmlView(TemplateView):
    template_name = 'home.html'


class DocumentView(TemplateView):
    template_name = 'document.html'

    def get_context_data(self, **kwargs):
        document = self.kwargs.get('doc', 'Index')
        return document_data(document)

# class DocumentView(TemplateView):
#     template_name = 'super.html'

#     def get_context_data(self, **kwargs):
#         menu = load_menu('README.md')
# #        sidemenu = load_side_menu('README.md')
#         doc = kwargs.get('doc', "README.md")
#         return dict(card=markdown_file_data(doc), menu=menu)
# #    , sidemenu=sidemenu)


# class CardView(TemplateView):
#     template_name = 'card.html'

#     def get_context_data(self, **kwargs):
#         data = dict(title="Card are Great", body=text)
#         return dict(card=data, title='Card View Layout')


# class CardsView(TemplateView):
#     template_name = 'cards.html'

#     def get_context_data(self, **kwargs):
#         return dict(cards=cards_data())


# class HomeView(TemplateView):
#     template_name = 'workshop.html'


class CardView(TemplateView):
    template_name = 'card.html'

    def get_context_data(self, **kwargs):
        return dict(cards=cards_data(), menu=load_menu('README.md'))


# class CardsView(TemplateView):
#     template_name = 'cards.html'

#     def get_context_data(self, **kwargs):
#         return dict(cards=cards_data(), menu=load_menu('README.md'))


# class TableView(TemplateView):
#     template_name = 'super.html'

#     def get_context_data(self, **kwargs):
#         return dict(title='Lessons Schedule',
#                     table=table_data('Documents/lessons.csv'),
#                     menu=load_menu('README.md'))


# class TabsView(TemplateView):
#     template_name = 'super.html'

#     def get_context_data(self, **kwargs):
#         tabs = tabs_data()
#         return dict(title='Tab View', tabs=tabs, menu=load_menu('README.md'))


# class CarouselView(TemplateView):
#     template_name = 'carousel.html'

#     def get_context_data(self, **kwargs):
#         carousel = carousel_data()
#         return dict(title='Carousel View', carousel=carousel, menu=load_menu('README.md'))


# class SuperView(TemplateView):
#     template_name = 'super.html'

#     def get_context_data(self, **kwargs):
#         return super_data()


# class AccordionView(TemplateView):
#     template_name = 'accordion.html'

#     def get_context_data(self, **kwargs):
#         return dict(accordion=accordion_data())
