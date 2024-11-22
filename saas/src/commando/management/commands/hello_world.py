from typing import Any
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Prints hello world to the console"

    def handle(self, *args: Any, **kwargs: Any):
        print("Hello world")
