from django.contrib.admin import AdminSite
from django.contrib import admin
import core.models as core_models


class VincentAdminSite(AdminSite):
    site_header = "Vincent test app administration"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._registry.update(admin.site._registry)

site = VincentAdminSite()

site.register(core_models.TODOModel)
