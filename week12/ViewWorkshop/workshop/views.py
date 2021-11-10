from django.views.generic import TemplateView
from os import listdir
from markdown import markdown
from django.views.generic import TemplateView

from .workshop import accordion_data, cards_data, carousel_data, document_data, table_data, tabs_data


class AccordionView(TemplateView):
    template_name = 'accordion.html'

    def get_context_data(self, **kwargs):
        return dict(accordion=accordion_data())


class DocumentView(TemplateView):
    template_name = 'document.html'

    def get_context_data(self, **kwargs):
        document = self.kwargs.get('doc', 'Index')
        return document_data(document)


class CardView(TemplateView):
    template_name = 'card.html'

    def get_context_data(self, **kwargs):
        return dict(cards=cards_data())


class CarouselView(TemplateView):
    template_name = 'carousel.html'

    def get_context_data(self, **kwargs):
        carousel = carousel_data()
        return dict(title='Carousel View', carousel=carousel)


class HtmlView(TemplateView):
    template_name = 'home.html'


class TableView(TemplateView):
    template_name = 'table.html'

    def get_context_data(self, **kwargs):
        return dict(title='Lessons Schedule',
                    table=table_data('Documents/lessons.csv'))


class TabsView(TemplateView):
    template_name = 'tabs.html'

    def get_context_data(self, **kwargs):
        tabs = tabs_data()
        return dict(title='Tab View', tabs=tabs)


# class SuperView(TemplateView):
#     template_name = 'super.html'

#     def get_context_data(self, **kwargs):
#         return super_data()
