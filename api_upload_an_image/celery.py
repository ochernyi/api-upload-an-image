from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api_upload_an_image.settings")
app = Celery("imageuploadapi")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
