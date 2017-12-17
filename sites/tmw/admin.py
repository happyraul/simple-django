from django.contrib import admin as _admin

from . import models as _models

_admin.site.register(_models.Site)
_admin.site.register(_models.Value)

