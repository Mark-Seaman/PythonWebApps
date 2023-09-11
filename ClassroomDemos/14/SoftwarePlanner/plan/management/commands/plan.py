from django.core.management.base import BaseCommand

from plan.views_plan import plan


class Command(BaseCommand):

    def handle(self, *args, **options):
        plan()
