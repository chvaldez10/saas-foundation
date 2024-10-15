from typing import Any
from django.conf import settings
from django.core.management.base import BaseCommand

# helper functions
from helpers import download_to_local

VENDOR_STATICFILES = {
    "flowbite.min.css": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css",
    "flowbite.min.js": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js",
}

STATICFILES_VENDOR_DIR = getattr(settings, "STATICFILES_VENDOR_DIR")

class Command(BaseCommand):
    help = "Downloads vendor files"

    def handle(self, *args: Any, **kwargs: Any):
        self.stdout.write("Downloading vendor files")
        completed_downloads = []
        
        for name, url in VENDOR_STATICFILES.items():
            output_path = STATICFILES_VENDOR_DIR / name
            download_success = download_to_local(url, output_path)

            if download_success:
                completed_downloads.append(url)
            else:
                self.stdout.write(self.style.ERROR(f"Failed to download {url}"))